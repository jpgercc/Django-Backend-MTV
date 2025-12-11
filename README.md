# bibliotecaapp (BACK-END)
<h2>Check the front-end <a href='https://github.com/jpgercc/Django-Frontend-MTV'>here</a></h2>

<a href='https://drive.google.com/drive/u/0/folders/1w9LtnXG0-5F2TAQ2sjCWCvN2RT4I_v6S'>DRIVE - TUTORIAIS</a>

<details>

<summary><b>TO DO</b></summary>

- [x] Relação many-to-many (feito em emprestimo (criado campo exemplares_renovados) )
- [x] Branches
- [ ] Pupular DB 

</details>

<img width="1530" height="912" alt="Image" src="https://github.com/user-attachments/assets/4eea1534-1a18-4480-9d09-ca4626a7dad8" />

<details>

<summary>CÓDIGO UML</summary>

O código UML abaixo tem as mesmas relações e atributos, porem tem os métodos simplificados e alguns detalhes a mais para melhorar a visualisação.

```uml
@startuml
class Emprestimo {
data_emprestimo: DateTime
data_devolucao_prevista: DateTime
data_devolucao_real: DateTime
status: String
renovacoes_realizadas: Integer
max_renovacoes: Integer
-usuario: Usuario
-funcionario: Funcionario
-exemplar: Exemplar
+toString()
}
class Usuario {
nome: String
email: String
telefone: String
endereco: String
data_cadastro: DateTime
ativo: Boolena
total_emprestimos: Integer
emprestimos_atrasados: Integer
total_atrasos_historico: Integer
data_ultimo_emprestimo: DateTime
limite_emprestimos: Integer
+toString()
}
class Funcionario {
nome: String
email: String
telefone: String
cargo: String
data_admissao: Date
ativo: Boolean
-bilioteca: Biblioteca
+toString()
}
class Autor {
nome: String
nacionalidade: String
data_nascimento: Date
sexo: String
}
class Editora {
nome: String
cnpj: String
endereco: String
telefone: String
}
class Exemplar {
codigo_de_barras: String
data_aquisicao: Date
estado_conservacao: String
localizacao: String
disponivel: Boolean
observacoes: Text
-biblioteca: Biblioteca
-livro: Livro
}
class Livro {
isbn: String
titulo: String
ano_publicacao: Integer
edicao: String
sinopse: Text
capa_rul
-autor: Autor
-editora: Editora
+toString()
}
class Biblioteca {
nome: String
endereco: String
telefone: String
catalogo: List<Livro>
+toString
}

Biblioteca *--> Funcionario
Biblioteca *--> Exemplar

Usuario *--> Emprestimo
Funcionario *--> Emprestimo
Exemplar *--> Emprestimo

Livro *--> Exemplar

Autor *--> Livro
Editora *--> Livro

@enduml
```

Apesar os mesmos atributos o diagrama acima não fica igual o da página base do README.md, aqui esta a representação visual do diagrama acima:

<img width="788" height="955" alt="Image" src="https://github.com/user-attachments/assets/d43a6eb0-61fd-4b5f-9001-76e292f8d7e9" />

</details>
