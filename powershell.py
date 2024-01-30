import string
import random
from base import BaseVarObf, BaseValObf, BaseAddComment


class PowershellVarObf(BaseVarObf):
    def _get_var_reg(self) -> str:
        return r"(?<!\$)\$(?!(?:null|true|false)\b)[a-zA-Z_][a-zA-Z0-9_]*" #r"\$(\w+)"

    def _get_pre_varchange_len(self):
        return len(self.content)
    
    def generate_varname(self):
        return f"${super().generate_varname()}"


class PowershellValObf(BaseValObf):
    def replace_false(self, match):
        alternates = ["!$True", "[bool]$null", f"![bool]({random.randint(1, 1000)})", "[bool](0)"]
        return random.choice(alternates)
    
    def replace_true(self, match):
        alternates = ["!$False", "![bool]$null", f"[bool]({random.randint(1, 1000)})", "![bool](0)"]
        return random.choice(alternates)
    
    def replace_null(self, match):
        fun_name = ''.join((random.choice(string.ascii_letters) for i in range(random.randint(5,10))))
        alternates =  [
                        "$(function "+ fun_name +" {})", 
                        f"$({random.randint(1,1000)} -as [void])", 
                        f"$({random.randint(1,1000)} -as [System.DBNull])"
                      ]
        return random.choice(alternates)
    
    def get_value_dict(self) -> dict:
        return {
            r"(?<!\$)\$false\b": self.replace_false,
            r"(?<!\$)\$true\b": self.replace_true,
            r"(?<!\$)\$null\b": self.replace_null
            }


class PowershellAddComment(BaseAddComment):
    def _comment_add_func(self, match):
        return f"<#{super()._comment_add_func(match)}#>\n"


def process_ps(args):
    input_file = args.input
    content = open(input_file, 'r').read()
    negetropy = int(args.negetropy)
    size = args.size 
    out_file = args.out

    varobf_input_size = None
    if size:
        varobf_input_size = int(float(size) * 0.7)
    varobf = PowershellVarObf(content, size=varobf_input_size, negetropy=negetropy)
    out_content = varobf.get_var_changed()
    if args.add_comment:
        addcomment = PowershellAddComment(out_content, negetropy=negetropy, size=int(size))
        out_content = addcomment.add_comments()
    
    if args.change_value:
        valobf = PowershellValObf(out_content)
        out_content = valobf.get_valchanged()
    
    if not out_file:
        if ".ps1" in input_file:
            out_file = input_file.replace(".ps1", ".obf.ps1")
        else:
            out_file = input_file + ".obf.ps1"
    
    open(out_file, 'w').write(out_content)
    print(f"output saved to: {out_file}")