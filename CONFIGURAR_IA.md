# 🤖 Como Configurar o Assistente IA

## 📝 Passo a Passo Rápido

### 1️⃣ Obter Chave API do Google Gemini (GRÁTIS)

1. Acesse: **https://makersuite.google.com/app/apikey**
2. Faça login com sua conta Google
3. Clique em **"Create API Key"** ou **"Get API Key"**
4. Copie a chave gerada (algo como: `AIzaSyB...`)

### 2️⃣ Configurar no Projeto

1. Abra o arquivo: **`.streamlit/secrets.toml`**
2. Substitua `COLE_SUA_CHAVE_API_AQUI` pela sua chave real
3. Salve o arquivo (Ctrl+S)

**Exemplo:**
```toml
GEMINI_API_KEY = "AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 3️⃣ Reiniciar o Dashboard

No terminal onde o Streamlit está rodando:
- Pressione **R** (reload)
- Ou feche e execute: `streamlit run app.py`

### 4️⃣ Testar

1. Acesse a seção **"🤖 Assistente IA"** no dashboard
2. Se configurado corretamente, verá a interface de chat
3. Teste com uma pergunta: *"O que é correlação?"*

---

## ⚠️ Solução de Problemas

### ❌ "API Key não configurada"
- Verifique se colou a chave corretamente em `secrets.toml`
- Certifique-se de que não há espaços extras antes/depois da chave
- Confirme que salvou o arquivo

### ❌ "Erro ao gerar resposta"
- Verifique sua conexão com a internet
- Confirme que a chave API é válida
- Tente gerar uma nova chave no Google AI Studio

### ❌ Streamlit não reconhece o arquivo
- Certifique-se de que o arquivo está em: `.streamlit/secrets.toml`
- Verifique se o nome está correto (sem .example)
- Reinicie completamente o Streamlit

---

## 🔒 Segurança

- ✅ O arquivo `secrets.toml` está no `.gitignore`
- ✅ Sua chave API **não será enviada ao GitHub**
- ✅ Mantenha sua chave privada e não compartilhe

---

## 💡 Dicas

### Limite Gratuito do Gemini
- **60 requisições por minuto**
- **1500 requisições por dia**
- **Mais que suficiente para uso acadêmico!**

### Alternativa: Variável de Ambiente
Você também pode configurar via variável de ambiente:
```powershell
$env:GEMINI_API_KEY = "sua-chave-aqui"
```

---

## 📞 Suporte

Se tiver problemas, verifique:
1. Console do Streamlit (terminal) para mensagens de erro
2. Se o arquivo `secrets.toml` está na pasta `.streamlit/`
3. Se a chave foi copiada completamente (sem quebras de linha)

**Status da configuração aparecerá automaticamente no dashboard!** ✨
