# Curso: Domine a Arquitetura Limpa e Hexagonal

Curso na plataforma Udemy, no qual toma base o livro Arquitetura Limpa. O curso se encontra neste [link](https://gbtech.udemy.com/course/arquitetura-limpa-e-hexagonal/learn/lecture/39303894?start=0#overview).

## Informações relevantes do curso

- Existem 3 camadas no conceito do software que devem ser levadas em consideração:
  - Arquitetura
  - Design 
  - Código

A exemplo, a Arquitetura Hexagonal, se diz respeito ao Design da aplicação. 

Conceitos de código não podem modificar a estrutura do Design, da mesma forma que o Design não pode influenciar no modo como é montada a Arquitetura.

### Principais paradigmas de programação

0. Programação NÃO Estruturada (GOTO)
1. Estruturado (EST)
2. Orientado a objetos (POO)
3. Funcional (PF)


#### 1. Paradigma Estruturado 

- Possuem estruturas de controle: (IF/ELSE/ELIF), (FOR/WHILE).
- Contém procedimentos, programação procedural com o intuito de encapsular o escopo específico em estruturas, diferentemente do GOTO onde tudo encontrava-se em sequência de linhas.
- Neste paradigma dá-se a ideia de **PILHA de execução** em que uma função pode chamar outra função, todavia ao término da função é necessário retornar ao ponto da função anterior. Esta ideia faz com qwe seja possível modularizar a aplicação. 

#### 2. Paradigma da Programação Orientado a objetos (POO)

A programação estruturada é a base do paradigma da POO. A programação orientada a objetos tem três pilares fundamentais (encapsulamento, hereança, polimorfismo).

- encapsulamento: é a capacidade de esconder detalhes de implementação e expor de forma mais simples para que um terceiro possa utilizar. Nem sempre um outro objeto que utilizar o objeto encasulado precisa conhecer todos os seus atributos e métodos. Exemplo: objeto carro esconde alguns métodos sobre o seu funcionamento que o objeto motorista não precisa cohecer para usar o carro, como a fim de explicação, o motorista não precisa conhecer detalhes do motor. 
- herança: serve para reuso de um objeto, sem ter a necessidade replicar o código. Perguntas feitas quando se pensa numa herança: **__ é um __?**, **__tem um __**? Exemplo: um civic é um carro? 
Tdavia, é preciso ressaltar dois aspectos: 
  - quando a pergunta for: __ é um __? Significa que esta relação é uma herança.
  - quando a pergunta for: __ tem um __? Significa que a relação é uma composiçãode objetos. Exemplo: o objeto carro tem um objeto motor? R: Sim. 
- polimorfismo: