# Git Rebase - Estudos

## Tipos de Rebase

### Rebase Padrao

Reaplica os commits do seu branch em cima de outro branch automaticamente, sem interacao.

```bash
git rebase main
```

O historico antes:

```
main:       A - B - C
                     \
meu-branch:           D - E - F
```

O historico depois:

```
main:       A - B - C - D' - E' - F'
```

Os commits viram `D'`, `E'`, `F'` porque sao commits novos com hash diferente, ja que o pai deles mudou.

### Rebase Interativo

Faz o mesmo processo, mas antes de comecar abre o editor e permite escolher o que fazer com cada commit.

```bash
git rebase -i HEAD~3
```

Acoes disponiveis no editor:

- `pick` - usa o commit como esta
- `reword` - usa o commit, mas edita a mensagem
- `squash` - une ao commit anterior
- `drop` - remove o commit

---

## Rebase vs Merge

| | Merge | Rebase |
|---|---|---|
| Cria merge commit | Sim | Nao |
| Historico | Preserva bifurcacoes | Linear |
| Reescreve historico | Nao | Sim |

O merge preserva a verdade historica. O rebase reescreve o historico como se tudo tivesse sido feito em sequencia.

---

## git commit --amend

Reescreve o ultimo commit local com um novo hash.

```bash
git commit --amend -m "nova mensagem"
```

Se o commit ja foi enviado ao remoto, o local e o remoto ficam com hashes diferentes e o historico ramifica. Para resolver isso, use `--force-with-lease`.

---

## git push --force-with-lease

Sobrescreve o remoto com o historico local de forma segura. Mais seguro que `--force` puro porque cancela se alguem tiver subido algo no remoto desde a sua ultima sincronizacao.

```bash
git push --force-with-lease
```

Usar o botao de sincronizar do VSCode ou `git pull` nesse cenario vai gerar um merge commit automatico e deixar o historico feio.

---

## Corrigindo historico bagunçado com rebase interativo

Cenario: voce fez `--amend` de um commit ja subido, depois fez `git pull` pelo VSCode e gerou um merge commit.

O historico ficou assim:

```
* a17c3cd Merge branch 'feat/...' of https://github.com/...
|\
| * a01c21e refactor: change name to s...
* | 29f2b43 refactor: change name of sum function to describe better the function
|/
* f4e222a feat: function to multiply two numbers
```

Para limpar:

```bash
git rebase -i HEAD~3
```

No editor, dropar o merge commit e o commit antigo, mantendo apenas o correto:

```
pick f4e222a feat: function to multiply two numbers
pick 29f2b43 refactor: change name of sum function to describe better the function
drop a01c21e refactor: change name to s...
```

Depois subir forcado:

```bash
git push --force-with-lease
```

---

## Configuracoes uteis

Abrir o editor do rebase no bloco de notas em vez do Vim:

```bash
git config --global core.editor notepad
```

Configurar pull para usar rebase em vez de merge por padrao:

```bash
git config --global pull.rebase true
```

---

## Regra de ouro

Nunca fazer rebase de commits que ja foram enviados ao remoto e que outras pessoas estao usando, pois voce estaria reescrevendo um historico que elas ja tem na maquina delas. Em branches proprias e exclusivas, e seguro.