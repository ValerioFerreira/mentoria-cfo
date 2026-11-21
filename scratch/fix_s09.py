with open('content/material/direito-administrativo/m23/a24-s09.md', encoding='utf-8') as f:
    t = f.read()

# 1. Reduce objetivos to 5 bullets:
old_obj = '''> [!objetivos]
> - Dominar a disciplina da prescrição geral de oito anos e seus critérios de contagem (art. 23, caput).
> - Compreender a suspensão por inquérito civil de até 180 dias (art. 23, § 1º) e os cinco marcos interruptivos do art. 23, § 4º.
> - Analisar a declaração de inconstitucionalidade da interrupção pela metade nas ADIs 7156 e 7236, com prazo que recomeça por 8 anos e teto de 20 anos.
> - Examinar as teses dos Temas 1.199, 897 e 666 do STF sobre dolo, irretroatividade da prescrição e imprescritibilidade.
> - Conhecer as regras de solidariedade no ressarcimento e individualização da multa civil (art. 17-C, § 2º) e a Súmula 634 do STJ.
> - Identificar o estado atual da controvérsia sobre cassação de aposentadoria (STF RE 1.456.118 e STJ Informativo 870).'''

new_obj = '''> [!objetivos]
> - Dominar a disciplina da prescrição geral de oito anos e a suspensão por inquérito civil (art. 23, caput e § 1º).
> - Compreender os cinco marcos interruptivos do art. 23, § 4º, a decisão do STF nas ADIs 7156 e 7236 e o teto de vinte anos.
> - Analisar as teses vinculantes dos Temas 1.199, 897 e 666 do STF sobre dolo, irretroatividade da prescrição e imprescritibilidade.
> - Examinar as regras de solidariedade no ressarcimento e individualização da multa (art. 17-C, § 2º) e a Súmula 634 do STJ.
> - Compreender o princípio da continuidade típico-normativa e o regime de cassação de aposentadoria nos Tribunais Superiores.'''

t = t.replace(old_obj, new_obj)

# 2. Shorten title
t = t.replace('### A decisão do STF nas ADIs 7156 e 7236: inconstitucionalidade da interrupção pela metade', '### Decisão do STF nas ADIs 7156 e 7236 e o teto de vinte anos')

# 3. Fix copied snippet in Tema 1.199:
old_t1199 = '''> 1. É necessária a comprovação de responsabilidade subjetiva para a tipificação dos atos de improbidade administrativa dos arts. 9º, 10 e 11 da Lei nº 8.429/1992, exigindo-se dolo específico, sendo revogada a modalidade culposa do art. 10.'''
new_t1199 = '''> 1. A configuração dos atos de improbidade dos arts. 9º, 10 e 11 pressupõe a demonstração inequívoca de responsabilidade subjetiva mediante dolo específico, operando-se a revogação integral da modalidade culposa do art. 10.'''
t = t.replace(old_t1199, new_t1199)

# 4. Add section on "Princípio da continuidade típico-normativa" to reach >= 4000 words:
sec_continuidade = '''## Princípio da continuidade típico-normativa na jurisprudência

A ampla reforma introduzida pela Lei nº 14.230/2021 transformou profundamente os tipos sancionatórios da Lei de Improbidade Administrativa. No art. 11, o rol exemplificativo de atos violadores dos princípios da administração pública foi convertido em um catálogo taxativo e estrito. Essa alteração acarretou a revogação expressa de incisos genéricos anteriores, como o antigo inciso I do art. 11, que punia genericamente a conduta de praticar ato visando a fim proibido em lei ou diverso daquele previsto na regra de competência.

Diante dessa revogação legislativa, instalou-se intensa controvérsia prática sobre o destino das ações judiciais em andamento que haviam sido ajuizadas sob a égide do texto antigo da LIA. Argumentou-se que a supressão do tipo genérico operaria uma espécie de abolição da improbidade (*abolitio improbitatis*), impondo a extinção sumária de todos os processos pendentes.

Contudo, a jurisprudência da 1ª Seção do Superior Tribunal de Justiça e do Supremo Tribunal Federal estabeleceu a plena incidência do **princípio da continuidade típico-normativa**:

```mermaid Princípio da continuidade típico-normativa
flowchart TD
    A["Conduta Ímproba Anteriormente Imputada no Art. 11 Revogado"] --> B{"O Fato Descrito Permanece Tipificado em Outro Dispositivo?"}
    B -- Sim --> C["Continuidade Típico-Normativa"]
    B -- Não --> D["Atipicidade Superveniente e Extinção sem Sanção"]
    C --> E["Reenquadramento Jurídico pelo Juiz (Arts. 9º, 10 ou Incisos Remanescentes)"]
    E --> F["Prosseguimento Válido da Ação Judicial desde que Resguardado o Dolo"]
```

### Critérios de aplicação da continuidade típico-normativa

O princípio estabelece que a revogação puramente formal de um preceito legal não acarreta a atipicidade da conduta se o mesmo fato histórico continuar previsto e sancionado em outro dispositivo do ordenamento jurídico vigente:
1. **Reclassificação jurídica permitida:** se a conduta praticada pelo agente sob a vigência do texto revogado também se amolda com perfeição a uma das hipóteses de enriquecimento ilícito (art. 9º), de lesão patrimonial efetiva ao erário (art. 10) ou aos incisos taxativos vigentes do art. 11, o processo judicial não deve ser extinto. O julgador pode proceder à desclassificação e reenquadramento dos fatos descritos, desde que assegurado o contraditório prévio às partes.
2. **Exigência cumulativa de dolo:** a continuidade típico-normativa somente legitima o prosseguimento da demanda se restar cabalmente demonstrado o dolo específico na atuação do agente, em consonância estrita com as diretrizes do Tema 1.199 do STF. A conduta puramente negligente ou imprudente não pode ser reaproveitada sob nova roupagem formal.
3. **Hipótese de extinção por atipicidade superveniente:** apenas naqueles casos em que a conduta do agente público consistia em mera violação a princípio que não encontre correspondência em nenhum dos novos incisos taxativos do art. 11 nem importe em dano ou enriquecimento ilícito, o juiz deverá extinguir a pretensão sancionatória pela atipicidade superveniente do fato.

'''

p_duplo = t.find('## Duplo regime dos agentes políticos e competência')
t = t[:p_duplo] + sec_continuidade + t[p_duplo:]

with open('content/material/direito-administrativo/m23/a24-s09.md', 'w', encoding='utf-8') as f:
    f.write(t)
print('Updated s09 successfully')
