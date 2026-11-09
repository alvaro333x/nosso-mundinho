# Plano de game design: profissões, casa e economia (a partir da v7.5)

Roleplay de casal: a gente trabalha, ganha moedinhas, melhora o trabalho, aumenta a casa e decora. O que está pronto vai marcado com a versão.

## Ideia central (pedido do Alvaro)
Começamos com quase nada e vamos evoluindo o mundinho: trabalhar, juntar moedinhas e desbloquear casa maior, quarto gamer, PCs, jogos, móveis, roupas, bichinhos, horta. Tudo que hoje já existe vira coisa conquistada.

## Quarto gamer — v7.6
- Cômodo da casa comprado com moedinhas. Cada um compra o seu PC gamer; os minigames abrem por dentro do PC (área de trabalho com os jogos). Cada jogo é comprado/desbloqueado.
- O Parque Radical e as barraquinhas saem do mapa.

## Loop do dia
1. Entrar, pegar a renda de quem trabalhou enquanto estávamos fora e pagar os salários do dia.
2. Trabalhar (cada um no seu cantinho do Predinho, lado a lado): Leticia atende pacientes, Alvaro entrega freelas.
3. Fazer as 3 missões do dia juntos (sequência 🔥).
4. Gastar: melhorias do trabalho, móveis, roupas, pets e a próxima etapa da casa.

## Predinho (área de trabalho) — v7.5
- Prédio no sudoeste do mundinho (`WORK3`), interior em x = -200 (`OF3`), mesma ideia da casa (teleporte pela porta).
- Metade esquerda: consultório da Leticia. Metade direita: estúdio do Alvaro. Parede de vidro no meio, hall com café.
- Estado de cada profissão em `S.job[i]` e no doc `trab/pN` (cada celular escreve só o seu; o outro só lê e desenha).
- Carinho no expediente: levar café (bônus de 10 min pro outro), ver o outro trabalhando, pets visitam.

## Consultório da Leticia — v7.5
- Pacientes têm ficha (peso, altura, meta, histórico), tipo (reeducação, emagrecimento, hipertrofia, criança, gestante, diabético, idoso, mãe com bebê) e condições extras (lactose, glúten, vegetariano, pressão alta).
- Consulta em 3 passos: anamnese (perguntas limitadas revelam saúde, gostos e aversões) → plano alimentar (escolher um prato por refeição até as metas ficarem verdes) → orientação (pergunta rápida).
- Nota da consulta vira estrelas, moedinhas, XP, adesão. A adesão decide o resultado no retorno (horas depois, de verdade): o peso muda e o corpo do boneco muda junto. Meta batida = alta, bônus, avaliação e indicação.
- Evolução: nível (30), reputação (média das últimas 20), equipamentos com bônus (16), funcionários com salário diário (recepcionista, estagiária, nutri associada com renda passiva de até 8 h).
- Números: consulta paga ~15 🪙 no começo e ~100 no fim; equipamentos de 120 a 5000 🪙; salários de 30 a 120 🪙/dia.

## Estúdio do Alvaro — v7.6
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
