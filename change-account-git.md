# Trocar de Conta no Git

Passo a passo para trocar rapidamente de conta no Git com GitHub.

---

## 1. Ver a conta logada atualmente

```bash
git credential-manager github list
```

---

## 2. Deslogar da conta atual

```bash
git credential-manager github logout seuUsuarioAqui
```

---

## 3. Atualizar nome e email globais

```bash
git config --global user.name "Thiago Rodrigo"
git config --global user.email "throdrigoms@gmail.com"
```

---

## 4. Verificar se foi aplicado

```bash
git config --global user.name
git config --global user.email
```

---

## 5. Forçar o Git a pedir login com a nova conta

```bash
git pull
```

Na proxima operacao com o remoto, o popup de autenticacao do GitHub vai abrir para voce logar com a nova conta.

---

## 6. Confirmar a conta logada

```bash
git credential-manager github list
```