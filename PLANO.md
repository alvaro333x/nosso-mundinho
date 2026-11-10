# Plano de game design: profissões, casa e economia (a partir da v7.5)

Roleplay de casal: a gente trabalha, ganha moedinhas, melhora o trabalho, aumenta a casa e decora. O que está pronto vai marcado com a versão.

## Ideia central (pedido do Alvaro)
Começamos com quase nada e vamos evoluindo o mundinho: trabalhar, juntar moedinhas e desbloquear casa maior, quarto gamer, PCs, jogos, móveis, roupas, bichinhos, horta. Tudo que hoje já existe vira coisa conquistada.

## Nossa história (a espinha do jogo)
Abertura tipo filme, na primeira vez: Alvaro no avião olhando pela janela → aeroporto, o primeiro encontro e o abraço → cenas curtas de dias felizes (praia, sorvete, pôr do sol) → jardim florido, ele se ajoelha, chora, pede a Leticia em namoro e dá a aliança → "e assim começou o nosso mundinho".
Capítulos, cada um com objetivos pagos com moedinhas e coisas que destravam:
1. **Namoro**: começamos com quase nada (casinha simples). Trabalhar, juntar, primeiros móveis, quarto gamer, bichinho.
2. **Morar juntos**: aumentar a casa, guarda-roupa, cozinha, horta, noites de filme.
3. **Construir**: melhorar o trabalho, a empresa, o consultório, o casarão.
4. **Casamento** (o grande objetivo): pagar aos poucos alianças, vestido, terno, festa, igreja católica; cerimônia jogável.
5. **Família**: quarto do bebê, filho.

## Relógio do jogo — próxima
O jogo tem o próprio tempo (um dia do jogo dura bem menos que um dia real e é igual nos dois celulares). De dia o consultório abre e a gente trabalha; de noite dá sono, e dormir juntos faz a noite passar. Disposição cai ao longo do dia e volta dormindo; trabalhar com sono rende menos.

## Mundinho do zero — v7.8 (feito; enriquecer aos poucos)
Pedido: começar sem nada mesmo, só o trabalho e a casinha pobre, e ir evoluindo tudo (até o lago é comprado). Refazer o mundo do zero.
- **Era nova**: carteira zerada, nada desbloqueado, móveis e bichinhos antigos saem (lembranças ficam: sequência, datas, álbum, cartas, chat, quadros, nível do trabalho). Marca de era nos docs (`era`), pra valer nos dois celulares.
- **Estado inicial**: barraquinho de madeira (por dentro: sala vazia, 2 sacos de dormir, um lampião, uma caixa de papelão), o Predinho pra trabalhar, um caminho de terra e mato em volta.
- **Como evolui**: placas de terreno no mundo ("Aqui vai o lago · 3000") e o catálogo 🏗️ Construir. Comprou, o mundinho recarrega com a obra pronta e uma festinha; o outro celular recebe o aviso e atualiza quando estiver livre.
- **Casa** (por fora e por dentro): barraquinho → casinha de madeira (300) → casa com sala (1200) → sobrado (4500) → casarão do Diário de uma Paixão (15000). Cômodos entram conforme a casa cresce: quarto gamer e quarto do casal com guarda-roupa (casa com sala), cozinha (sobrado), quartinho do bebê (casarão, capítulo família).
- **Dentro de casa**: saco de dormir → colchão → cama; TV, sofá, estante, tapete, mesa: tudo comprado.
- **Terreno**: caixinha de correio, postes de luz, rede, canteiros do jardim (um por um), hortinha, fonte, pracinha, ateliê, lago (cavar) → píer → vara de pesca → barquinho → cisnes.
- **Loja de pets**: feita na v7.10 como o cantinho dos pets do mercadinho (cercadinhos, tia atendente, preço por raridade).
- **Técnica**: desbloqueios em `casal/pN.unl` com chaves `w:<obra>`; `buildWorld` monta só o que existe (terreno sem a cova do lago, sem colisão do que não foi construído); união dos desbloqueios guardada localmente pra saber o que montar antes da rede conectar.

## Vilinha e Mercadinho — v7.10 (feito; enriquecer aos poucos)
- Mapa em volta da pracinha: casa ao norte, Predinho a oeste, Mercadinho a leste, lago ao sul, jardim e ateliê dos lados da casa. Ruas em cruz, bancos, vasos, placa de direções.
- Mercadinho por dentro: pega o carrinho, passeia pelos corredores (hortifruti, padaria, bebidas, doces, presentes, pets, utilidades, chapéus, decoração, móveis), paga no caixa com a atendente. Nada mais é comprado por menu.
- Utilidade: comida dá disposição (pra trabalhar bem sem dormir toda hora), presente se entrega pro outro (carinho + missão), ração vai pra despensa dos bichinhos, móveis vão pra casa.
- Próximas ideias: promoção do dia, lista de compras como missão, sementes da hortinha, roupas (jaleco da Leticia), cesta de piquenique, pipoca pro filme, ingredientes pra cozinhar em casa.

## Academia do Alvaro — v7.12 (feito; aprofundar)
- Lado direito do Predinho. O Alvaro é personal: aluno chega, avaliação (2 perguntas), treino com 5 exercícios que batem os 3 objetivos sem forçar onde dói, aula acompanhada nos aparelhos, resultado. O aluno evolui a cada aula (o corpo muda) até bater a meta.
- Aparelhos comprados liberam exercícios; nível libera tipos de aluno (iniciante, emagrecer, massa, condicionamento, postura, terceira idade).
- O casal também treina nos aparelhos (missão do dia).
- Próximos passos: alunos visíveis nos dois celulares, aula em dupla com a Leticia (nutri + personal pro mesmo paciente/aluno), mais aparelhos, estagiário, campeonato.

## Pedidos de 09/11 à noite (fila)
- Sem emoji em lugar nenhum: arte própria (feito no mercadinho na v7.11; falta o resto).
- Produtos em 3D nas prateleiras (feito na v7.11).
- Bichinhos mais fofos e em proporção (proporção feita; redesenho ou modelos prontos depende de autorização pra baixar arquivos).
- Academia: o Alvaro vira personal trainer, com alunos, fichas, treinos, evolução e máquinas funcionando, ao lado do consultório.
- Mais conteúdo e objetivos longos pro jogo não acabar rápido.

## Quarto gamer — v7.6
- Cômodo da casa comprado com moedinhas. Cada um compra o seu PC gamer; os minigames abrem por dentro do PC (área de trabalho com os jogos). Cada jogo é comprado/desbloqueado.
- O Parque Radical e as barraquinhas saem do mapa.

## Loop do dia
1. Entrar, pegar a renda de quem trabalhou enquanto estávamos fora e pagar os salários do dia.
2. Trabalhar (cada um no seu cantinho do Predinho, lado a lado): Leticia atende pacientes, Alvaro entrega freelas.
3. Fazer as 3 missões do dia juntos (sequência 🔥).
4. Gastar: melhorias do trabalho, móveis, roupas, pets e a próxima etapa da casa.

## Predinho (área de trabalho) — v7.5
- Prédio a oeste da pracinha (`WORK3`), interior em x = -200 (`OF3`), mesma ideia da casa (teleporte pela porta).
- Metade esquerda: consultório da Leticia. Metade direita: estúdio do Alvaro. Parede de vidro no meio, hall com café.
- Estado de cada profissão em `S.job[i]` e no doc `trab/pN` (cada celular escreve só o seu; o outro só lê e desenha).
- Carinho no expediente: levar café (bônus de 10 min pro outro), ver o outro trabalhando, pets visitam.

## Consultório da Leticia — v7.5
- Pacientes têm ficha (peso, altura, meta, histórico), tipo (reeducação, emagrecimento, hipertrofia, criança, gestante, diabético, idoso, mãe com bebê) e condições extras (lactose, glúten, vegetariano, pressão alta).
- Consulta em 3 passos: anamnese (perguntas limitadas revelam saúde, gostos e aversões) → plano alimentar (escolher um prato por refeição até as metas ficarem verdes) → orientação (pergunta rápida).
- Nota da consulta vira estrelas, moedinhas, XP, adesão. A adesão decide o resultado no retorno (horas depois, de verdade): o peso muda e o corpo do boneco muda junto. Meta batida = alta, bônus, avaliação e indicação.
- Evolução: nível (30), reputação (média das últimas 20), equipamentos com bônus (16), funcionários com salário diário (recepcionista, estagiária, nutri associada com renda passiva de até 8 h).
- Números: consulta paga ~15 🪙 no começo e ~100 no fim; equipamentos de 120 a 5000 🪙; salários de 30 a 120 🪙/dia.

## Trabalho do Alvaro
O trabalho dele é dele (não é assistente do consultório) e é no PC, mas sem exigir programação de verdade: estúdio de apps com IA. Cada cliente: montar o pedido pra IA com os blocos certos, testar achando o que saiu bugado, publicar na hora certa. Crescer com clientes fixos, upgrades do PC, equipe e empresa. O texto abaixo era o plano antigo e ficou só de registro.

## (antigo) Estúdio do Alvaro
- Mural de freelas (cliente, tipo, tarefas, prazo de verdade, pagamento). Cada tarefa é um minijogo curto: caça-bug, montar o código, ligar os canos (deploy) e revisão relâmpago (verdadeiro ou falso de JS).
- Tarefa mal feita vira bug que o cliente reclama depois. Entrega no prazo dá gorjeta, avaliação e cliente que volta com projeto maior.
- Evolução: PC gamer (placa, monitores, teclado, cadeira, RGB…), equipe (estagiário, dev, designer, QA), etapas da empresa (freelancer → estúdio → startup → empresa) com produto próprio de renda passiva.

## Casa que evolui — v7.7
- Etapas compradas com moedinhas, por fora e por dentro: cabana → casinha → sobrado → casarão do Diário de uma Paixão (o final).
- Cada etapa aumenta a sala, libera cômodos e espaço pra móveis. Papel de parede e piso trocáveis.
- Mundo reorganizado junto: caminhos, placas, mapa com teleporte, HUD arrumada.
- Mundinho que cresce com o dinheiro: os minigames viram atrações compradas (cada portal/barraquinha começa "em obras" com placa de preço) e ficam todos numa área só deles, bem desenhada.

## Vida a dois — v7.8
- Depois do expediente: noite de filme deitados no sofá (conchinha), fazer pipoca na cozinha da casa, piquenique no gramado com cesta comprada na lojinha, jantar à luz de velas.
- Cada programa custa um pouquinho (milho de pipoca, cesta, velas) e devolve em carinho: bônus de ânimo pro trabalho do dia seguinte, missões e conquistas do casal.

## Economia
- Ganhos: missões (30 cada + bônus), trabalho (principal), cozinha, pesca, jardim, jogos.
- Gastos por faixa: até 200 (móveis, chapéus, comida de pet), 200–2000 (equipamentos, roupas, temas), 2000–10000 (salas, etapas da casa, empresa), sonhos acima de 10000.
- Renda passiva existe (funcionários), mas com teto de 8 h e salário por dia jogado, pra nunca render mais que jogar.
