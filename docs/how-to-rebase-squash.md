# Git Rebase - Squash e Fixup

## Acoes do rebase interativo

```bash
git rebase -i HEAD~3
```

| Acao | Comportamento |
|---|---|
| pick | usa o commit como esta |
| reword | usa o commit, mas edita a mensagem |
| squash | une ao commit anterior, abre editor pra escolher a mensagem final |
| fixup | une ao commit anterior, descarta a mensagem do commit unido |
| drop | remove o commit |
| edit | pausa o rebase e permite alterar o commit manualmente |
| exec | executa um comando shell apos o commit |

---

## Squash

Une o commit ao que esta imediatamente acima na lista. O primeiro da sequencia precisa ser `pick`.

```
pick f4e222a feat: function to multiply two numbers
squash 21ec13c chore: add description of function sum
squash c018928 chore: add description of function multiplication
```

Abre o editor com todas as mensagens e deixa voce escrever a mensagem final.

---

## Fixup

Igual ao squash, mas descarta automaticamente a mensagem do commit unido, ficando so com a do `pick`.

```
pick f4e222a feat: function to multiply two numbers
fixup 21ec13c chore: add description of function sum
fixup c018928 chore: add description of function multiplication
```

Nao abre editor, une silenciosamente.

---

## Atencao com hashes

O Git exige no minimo 7 caracteres no hash. Hash incompleto gera erro:

```
error: could not parse '018928'
```

Se isso ocorrer, aborte e verifique os hashes corretos:

```bash
git rebase --abort
git log --oneline
```

---

## Fluxo completo

```bash
git rebase -i HEAD~3
# editar o arquivo, salvar e fechar
git push --force-with-lease
```