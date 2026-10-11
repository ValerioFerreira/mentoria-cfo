# Procedimento de Backup e Restauração de Questões

Este diretório contém os backups estruturados das questões do sistema, incluindo enunciados, alternativas, justificativas, metadados, vínculos com disciplinas e segmentos, e histórico de respostas de usuários.

## 1. Geração de Backup

Para gerar um novo backup completo das questões e criar o manifesto de integridade:

```bash
npx --prefix web tsx ../scripts/backup_questions.ts
```

O script irá:
1. Exportar todas as questões da tabela `Question` e suas respectivas `QuestionOption`.
2. Exportar o histórico de respostas de simulados/cadernos (`QuizAnswer`) e sessões (`QuizSession`).
3. Gravar um arquivo JSON com timestamp em `backups/questoes/backup_questions_<timestamp>.json`.
4. Calcular o checksum SHA-256 e salvar o arquivo `manifest.json`.

## 2. Verificação de Integridade

Para conferir o hash SHA-256 e a estrutura do backup:

```bash
npx --prefix web tsx ../scripts/verify_backup.ts
```

O script confirmará se:
- O arquivo existe e possui o SHA-256 idêntico ao do manifesto.
- A contagem de questões e alternativas bate com o manifesto.
- Não há registros corrompidos ou incompletos.

## 3. Procedimento de Restauração

Caso seja necessário reverter ou restaurar as questões a partir de um backup:

```bash
# Para restaurar a partir do manifesto mais recente:
npx --prefix web tsx ../scripts/restore_backup.ts

# Para restaurar um arquivo específico:
npx --prefix web tsx ../scripts/restore_backup.ts backups/questoes/backup_questions_XXXX.json
```
