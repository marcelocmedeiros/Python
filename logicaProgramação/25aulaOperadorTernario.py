logged_user = True

if logged_user:
    msg = "Usuário logado"
else:
    msg = "Usuário pracisa logar"
print(msg)

# ternário

logged_user = False
msg = "Usuário logado" if(logged_user ) else("Usuário pracisa logar")