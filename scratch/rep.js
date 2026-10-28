// uso: node rep.js arquivo <<< JSON [[old,new],...]  (CRLF-safe; falha se old não for encontrado exatamente uma vez)
const fs=require("fs");const f=process.argv[2];
const pairs=JSON.parse(fs.readFileSync(0,"utf8"));
let s=fs.readFileSync(f,"utf8");const crlf=s.includes("\r\n");if(crlf)s=s.replace(/\r\n/g,"\n");
for(const [a,b] of pairs){const n=s.split(a).length-1;if(n!==1){console.error("ERRO: "+n+" ocorrências de: "+a.slice(0,60));process.exit(1);}s=s.replace(a,()=>b);}
if(crlf)s=s.replace(/\n/g,"\r\n");fs.writeFileSync(f,s);console.log("ok "+f);
