import re
import string
from abc import abstractmethod, ABC
import random

class BaseVarObf(ABC):
    """
    Base class for obfuscating variable names
    """
    def __init__(self,content, negetropy=1, size=None, change_str=True,
                 add_comment=True) -> None:
        self.content = content
        self.negetropy = negetropy
        self.size = size
        self.change_str = change_str
        self.add_comment = add_comment
        self.defined_vars = {}
        self._make_defined_vars()
    
    @abstractmethod
    def _get_pre_varchange_len(self):
        None

    @abstractmethod
    def _get_var_reg(self) -> str:
        None

    def _make_defined_vars(self):
        matches = re.finditer(self._get_var_reg(), self.content)
        for match in matches:
            if not match.group() in self.defined_vars:
                self.defined_vars[match.group()] = self.generate_varname()

    def _get_total_varsize(self):
        matches = re.findall(self._get_var_reg(), self.content)
        total_varsize = sum([len(var) for var in matches])
        return total_varsize

    def _var_replace_function(self, match):
        if match.group() in self.defined_vars:
            return self.defined_vars[match.group()]
        else:
            self.defined_vars[match.group()] = self.generate_varname()
            return self.defined_vars[match.group()]

    def num_vars(self):
        matches = re.finditer(self._get_var_reg(), self.content)
        return len(list(matches))

    def get_varsize(self):
        var_size = 10
        if self.size:
            before_size = self._get_pre_varchange_len()
            num_vars = self.num_vars()
            total_varsize = self._get_total_varsize()
            total_new_varsize = (self.size - (before_size - total_varsize))
            if total_new_varsize < 1:
                total_new_varsize = 1
            var_size = int(total_new_varsize / num_vars)
        if var_size < 1:
            var_size = 1
        return var_size
    
    def generate_varname(self):
        if not self.negetropy:
            self.negetropy = 1
        
        letters = string.ascii_lowercase + string.ascii_uppercase
        var_length = self.get_varsize()
        num_chars = int(var_length / self.negetropy)
        out = ''.join((random.choice(letters)*self.negetropy) for i in range(num_chars))
        rand_char = random.choice(letters)
        while len(out) < var_length:
            out = out + rand_char
        if out in self.defined_vars.values():
            return self.generate_varname()
        return out

    def get_var_changed(self):
        return re.sub(self._get_var_reg(), self._var_replace_function, self.content)
    

class BaseValObf(ABC):
    """
    Base class for obfuscating values
    """
    def __init__(self, content) -> None:
        self.content = content

    @abstractmethod
    def get_value_dict(self) -> dict:
        None

    def get_valchanged(self):
        val_dict = self.get_value_dict()
        for reg in val_dict:
            self.content = re.sub(reg, val_dict[reg], self.content)
        return self.content


class BaseAddComment:
    def __init__(self,content, add_comment=True, size=None, negetropy=1, comment_pos=[r"\n", r";"]) -> None:
        self.content = content
        self.add_comment = add_comment
        self.size = size
        self.negetropy = negetropy
        self.comment_pos = comment_pos
    
    def _comment_add_func(self, match):
        num_chars = int(self.comment_len / self.negetropy)
        rand_text = ''.join((random.choice(string.ascii_letters)*self.negetropy) for i in range(num_chars))
        return rand_text

    def add_comments(self):
        total_comment_size = None
        if self.size:
            total_comment_size = self.size - len(self.content)
        else:
            self.total_comment_size = 300
        if total_comment_size <= 0:
            total_comment_size = 10 
        comment_count = 0
        for pos in self.comment_pos:
            comment_count += len(re.findall(pos, self.content))
        if comment_count == 0:
            comment_count = 1
        self.comment_len = int(total_comment_size / comment_count)
        for pos in self.comment_pos:
            self.content = re.sub(pos, self._comment_add_func, self.content)
        return self.content