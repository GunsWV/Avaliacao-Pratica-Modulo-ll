import sqlite3

# 1️⃣ Conectar ao banco
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# 2️⃣ Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT
)
""")

# 3️⃣ Inserir registros
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("Maria Silva", 20, "maria@email.com"))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ("João Souza", 22, "joao@email.com"))
conn.commit()

# 4️⃣ Listar todos
print("📋 Lista de alunos:")
for row in cursor.execute("SELECT * FROM alunos"):
    print(row)

# 5️⃣ Buscar por ID
id_busca = 1
cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_busca,))
aluno = cursor.fetchone()
print(f"\n🔍 Aluno com ID {id_busca}: {aluno}")

# 6️⃣ Atualizar registro
novo_email = "maria.atualizado@email.com"
cursor.execute("UPDATE alunos SET email = ? WHERE id = ?", (novo_email, id_busca))
conn.commit()
print(f"\n✅ Aluno {id_busca} atualizado com sucesso!")

# Verificar atualização
cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_busca,))
print("🔁 Registro atualizado:", cursor.fetchone())

# 7️⃣ Deletar registro
id_excluir = 2
cursor.execute("DELETE FROM alunos WHERE id = ?", (id_excluir,))
conn.commit()
print(f"\n❌ Aluno com ID {id_excluir} excluído.")

# Listar registros após exclusão
print("\n📋 Lista após exclusão:")
for row in cursor.execute("SELECT * FROM alunos"):
    print(row)

# Fechar conexão
conn.close()