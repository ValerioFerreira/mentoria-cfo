with open("pipeline/check_citations.py", "r", encoding="utf-8") as f:
    c = f.read()

target = '    # "Art. 2º" não pode casar com "Art. 2º-C" (artigo acrescentado)\n    pat = re.compile(r"Art\\.? ?" + re.escape(num) + r"(º|o|°)?(?![\\d])(?!\\s?[-–]\\s?[A-Z])[-–.\\s]")'
# handle crlf
if "\r\n" in c:
    target = target.replace("\n", "\r\n")

replacement = '    # normaliza marcações de revogação parciais de HTML como [REVOGADO: Art.] [REVOGADO: 78.\n    text = re.sub(r"\\[REVOGADO:\\s*([^\\]]*)\\]", r"\\1", text)\n    # "Art. 2º" não pode casar com "Art. 2º-C" (artigo acrescentado)\n    pat = re.compile(r"Art\\.?\\s*" + re.escape(num) + r"(º|o|°)?(?![\\d])(?!-[A-Za-z]{1,2}\\b)[-–.\\s]")'
if "\r\n" in c:
    replacement = replacement.replace("\n", "\r\n")

if target in c:
    c = c.replace(target, replacement, 1)
    with open("pipeline/check_citations.py", "w", encoding="utf-8", newline="") as f:
        f.write(c)
    print("SUCCESS")
else:
    print("TARGET NOT FOUND")
