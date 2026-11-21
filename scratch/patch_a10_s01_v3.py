with open('content/material/direito-constitucional/m08/a10-s01.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace line 261
old_line = 'O art. 57, § 4º, estipula que cada Casa reúne-se em sessões preparatórias para a posse dos membros e eleição de suas Mesas "para mandato de 2 (dois) anos, **vedada a recondução para o mesmo cargo na eleição imediatamente subsequente**".'
new_line = 'O texto constitucional estabelece no art. 57, § 4º, que as Casas legislativas reúnem-se em sessões preparatórias para posse e escolha das Mesas para mandato de dois anos, impedindo-se a reeleição contígua para a mesma função diretiva.'
text = text.replace(old_line, new_line)

# Trim words
text = text.replace(
    'O estabelecimento de piso (8) e teto (70) ameniza a proporcionalidade pura, beneficiando unidades federadas de menor densidade demográfica (como os Estados da Região Norte) e limitando o poder numérico dos Estados mais populosos (como São Paulo).',
    'O piso de 8 e o teto de 70 atenuam a proporcionalidade pura, equilibrando a representação política dos Estados menos populosos frente aos grandes colégios eleitorais.'
)

text = text.replace(
    'O tamanho territorial, o peso econômico e a densidade demográfica do ente federado são desconsiderados: o Estado de menor população (Roraima) e o Estado mais populoso (São Paulo) possuem exatamente a mesma representação de três senadores. Eventuais Territórios Federais não elegem senadores, pois não ostentam autonomia federativa política.',
    'A representação é paritária: todos os Estados e o DF possuem rigorosamente três senadores, desconsiderando-se a densidade demográfica. Eventuais Territórios Federais não elegem senadores por não ostentarem autonomia política federativa.'
)

with open('content/material/direito-constitucional/m08/a10-s01.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated successfully via script')
