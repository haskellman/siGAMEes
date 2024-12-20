CHARACTERS_DATA = {
    'player': {
        'name': 'player',
		'dialog': {
            'default': ['Sim', 'Não'],
		'visited': False,
            },
        'questions': {},    
		},
    'vitor': {
		'name': 'Vitor',
		'dialog': {
            'default': ['então você conseguiu chegar até aqui!', 'devo parabenizá-lo por isso...', 'mas voce não vai conseguir minha chave tão facilmente', 'sou vitor, o javaboy', 'então voce quer minha chave? para isso você terá que me vencer em uma batalha de java!', 'vamos começar!!!'],
			'visited': ['parabéns!', 'você conseguiu mostrar domínio teórico em java', 'meus parabéns!', 'agora vá conseguir a aprovação da monalessa', 'sei que você consegue' ,'boa sorte!'],
            'end': ['ah, café... é mais que uma bebida, é uma arte! ', 'você já percebeu como cada xícara tem sua própria personalidade? ', 'quero dizer, o espresso é direto, intenso, como aquele amigo que fala a verdade sem rodeios.', 'já o latte... ah, é como um abraço quentinho, perfeito para dias de chuva.', 'ops!!!', 'parabéns por entrar no labes', 'tem café na geladeira!!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': '0',
        'questions': {
				0: {
					'title': 'Pergunta 1',
					'description':'O que é o Jakarta EE? ',
					'options': ['Um servidor de aplicação Java usado para hospedar aplicações Web. ',
                 				'Um conjunto de especificações para o desenvolvimento de aplicações escaláveis e distribuídas em Java. ',
                                'Uma ferramenta para gerenciar e construir projetos Java. ',
                            	'Um banco de dados relacional usado para armazenar dados do sistema. '],
                    'correct': 1,
                    'link': '0',
				},
				1: {
					'title': 'Pergunta: 2',
					'description':'O que a linguagem Java usa quando um objeto necessita acessar uma referência a si mesmo.',
					'options': ['new',
                 				'static',
                                'this',
                                'final'],
                    'correct': 2,
                    'link': '4',
				},
				2: {
					'title': 'Pergunta: 3',
					'description':'Qual a função do bloco finally?',
					'options': ['É Um bloco opcional que contém o código a ser executado sempre, independentemente de ocorrer ou não uma exceção. ',
                 			    'Um bloco reservado apenas para manipulação de erros críticos. ',
                                'Um bloco que só é executado se uma exceção for lançada. ', 
                                'Um bloco utilizado para interromper o fluxo do programa imediatamente ao encontrar uma exceção. '],
                    'correct': 2,
                    'link': '4',
				},
				3: {
					'title': 'Pergunta: 4',
					'description':'Qual a função de uma classe abstrata?',
					'options': ['Classe abstrata é um tipo de classe que não possui atributos.',
                 				'Classe abstrata é um tipo de classe que não possui métodos.',
                                'O código de uma classe abstrata deve ser escrito dentro de uma função main().',
                                'Não é possível criar um objeto de uma classe abstrata.'],
                    'correct': 3,
                    'link': '5',
				},
				4: {
					'title': 'Pergunta: 5',
					'description':'O que é Maven? ',
					'options': ['Uma ferramenta para construir, gerenciar e compartilhar projetos de software em Java',
                 				'Um servidor de aplicação para hospedar sistemas Java',
                                'Uma API que implementa o padrão RESTful em Jakarta EE',
                                'Um sistema gerenciador de bancos de dados'],
                    'correct': 0,
                    'link': '0',
				},
				5: {
					'title': 'Pergunta 6',
					'description':'Descreva brevemente o que é WildFly?',
					'options': ['Uma ferramenta para gerenciar dependências e construir projetos Java', 
								'Um servidor de aplicação Java que implementa as especificações do Jakarta EE', 
								'Uma API para criação de serviços Web RESTful em Java', 
								'Um banco de dados usado para armazenar classes de domínio'],
                    'correct': 1,
                    'link': '0',
				},
				6: {
					'title': 'Pergunta: 7',
					'description':'Qual desses componentes é responsável por armazenar e persistir os dados das classes de domínio? ',
					'options': ['SQL',
                 				'WildFly',
                                'PostgreSQL',
                                'Spring boot'],
                    'correct': 2,
                    'link': '0',
				},
				7: {
					'title': 'Pergunta: 8',
					'description':'O que é Docker?',
					'options': ['Docker é uma plataforma de virtualização de contêineres que permite que desenvolvedores empacotem suas aplicações em ambientes portáveis e autossuficientes que podem ser executados em qualquer lugar',
                 				'Docker é uma ferramenta para criar e gerenciar máquinas virtuais',
                                'Docker é um sistema operacional que roda dentro de outro sistema operacional',
                                'Docker é uma plataforma que permite o gerenciamento de máquinas virtuais, oferecendo uma interface gráfica para criar, configurar e monitorar sistemas e programas na nuvem.'],
                    'correct': 0,
                    'link': '5',
				},
				8: {
					'title': 'Pergunta: 9',
					'description':'Como você roda uma imagem Docker?',
					'options': ['docker start',
                 				'docker run',
                                'docker "image_name"',
                                'docker start "image_name"'],
                    'correct': 1,
                    'link': '5',
				},
				9: {
					'title': 'Pergunta: 10',
					'description':'O que é Docker Compose?',
					'options': ['É uma ferramenta que permite iniciar múltiplos contêineres Docker de uma vez, mas exige que todos os contêineres usem a mesma imagem base.',
                 				'É uma ferramenta que permite criar e gerenciar várias imagens Docker ao mesmo tempo, facilitando o armazenamento de imagens em repositórios locais.',
                                'É uma plataforma para armazenar imagens de contêineres na nuvem',
                                'É uma ferramenta que permite definir e rodar aplicações em vários containers'],
                    'correct': 3,
                    'link': '5',
				},
			},
		},
    'monalessa': {
		'name': 'Monalessa',
		'dialog': {
            'default': ['se você está aqui isso significa...', 'que você foi aprovado pelo java master, vitor', 'nada mal...', 'mas agora a coisa fica séria', 'eu sou a monalessa', 'e você vai ter que me provar que manja de git', 'vamos começar!!!'],
			'visited': ['meus parabéns!', 'você está quase pronto para entrar no labes', 'mas o teste final é com a patricia', 'ela não é fácil não mas...', 'eu acredito em você', 'boa sorte!'],
            'end': ['congratulações!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': '1',
        'questions': {
				0: {
					'title': 'Pergunta: 1',
					'description':'O que é o Git?',
					'options': ['Um sistema para criar e executar códigos automaticamente',
                 				'Um editor de texto avançado para programadores',
                                'Um sistema de controle de versão para gerenciar modificações em arquivos de código',
                                'Um software de gerenciamento de banco de dados'],
                    'correct': 2,
                    'link': '1',
				},
				1: {
					'title': 'Pergunta: 2',
					'description':'Qual comando é utilizado para iniciar um repositório Git em uma pasta nova?',
					'options': ['git start',
                 				'git init',
                                'git new',
                                'git repository'],
                    'correct': 1,
                    'link': '1',
				},
				2: {
					'title': 'Pergunta 3',
					'description':'Qual comando deve ser executado para obter as atualizações mais recentes de um repositório remoto?',
					'options': ['git pull',
                 				'git fetch',
                                'git update',
                                'git clone'],
                    'correct': 0,
                    'link': '1',
				},
				3: {
					'title': 'Pergunta: 4',
					'description':'Em qual situação é ideal criar uma nova branch?',
					'options': ['Quando você deseja atualizar o repositório com mudanças de outros usuários',
                 				'Quando precisa salvar suas mudanças localmente',
                                'Quando quer modificar o código sem alterar a versão principal até que a atualização esteja testada',
                                'Quando deseja deletar arquivos do repositório'],
                    'correct': 2,
                    'link': '1',
				},
				4: {
					'title': 'Pergunta: 5',
					'description':'Qual é a função principal do GitLab?',
					'options': ['Gerenciar bancos de dados para grandes empresas',
                 				'Oferecer uma plataforma DevOps completa para desenvolvimento e operação de software',
                                'Servir como editor de texto colaborativo para programadores',
                                'Servir como repositório de código colaborativo para programadores'],
                    'correct': 1,
                    'link': '2',
				},
				5: {
					'title': 'Pergunta: 6',
					'description':'Qual funcionalidade no GitLab permite gerenciar requisições de fusão e revisões de código?',
					'options': ['Repository > Files',
                 				'Issues > Boards',
                                'Project Information > Merge',
                                'Merge Requests'],
                    'correct': 3,
                    'link': '2',
				},
				6: {
					'title': 'Pergunta: 7',
					'description':'Qual opção permite que os usuários adicionem rótulos (labels) para organizar as tarefas de um projeto?',
					'options': ['Repository > Labels',
                 				'Project Information > Labels',
                                'Issues > Tags',
                                'Project Information > Members'],
                    'correct': 1,
                    'link': '2',
				},
				7: {
					'title': 'Pergunta: 8',
					'description':'Qual é o objetivo principal do GitLabES Flow?',
					'options': ['Facilitar o backup de projetos em nuvem',
                 				'Organizar o fluxo de trabalho de um time de desenvolvedores em torno de um repositório Git no GitLab',
                                'Configurar o GitLab para trabalhar com ferramentas externas como o Slack',
                                'Criar projetos automaticamente no GitLab'],
                    'correct': 1,
                    'link': '3',
				},
				8: {
					'title': 'Pergunta: 9',
					'description':'Quais etiquetas (labels) são recomendadas para indicar que uma tarefa está em andamento e pronta para revisão?',
					'options': ['Backlog e In Progress',
                 				'Review e Done',
                                'Ongoing e Review',
                                ' Sprint e Complete'],
                    'correct': 2,
                    'link': '3',
				},
				9: {
					'title': 'Pergunta: 10',
					'description':'Como você deve sinalizar que uma tarefa (issue) está pronta para revisão no GitLab?',
					'options': ['Atribuir a etiqueta Backlog',
                 				'Marcar a tarefa como Done',
                                'Atribuir a etiqueta Review e designar um revisor no merge request',
                                'Transferir a tarefa para a coluna Completed no quadro Kanban'],
                    'correct': 2,
                    'link': '3',
				},
				10: {
					'title': 'Pergunta: 11',
					'description':'Para que serve o botão Mark as ready em um merge request?',
					'options': ['Para marcar o merge request como concluído',
                 				'Para indicar que o merge request está pronto para revisão, saindo do estado de rascunho (Draft)',
                                'Para deletar o merge request',
                                'Para transferir o merge request para outro revisor'],
                    'correct': 1,
                    'link': '3',
				},
			},
		},
    'patricia': {
        'name': 'Patricia',
		'dialog': {
            'default': ['seja bem vindo!', 'então voce conseguiu vencer os meus colegas...', 'eles devem ter pegado leve com você', 'não espere o mesmo de mim haha', 'eu sou a patricia', 'está pronto para voltar pra casa chorando?',],
			'visited': ['uauu', 'voce conseguiu superar o meu desafio', 'você merece isso!', 'com isso você tem todas as chaves!', 'agora que desafio de verdade', 'você pode entrar no sigAmaes', 'boa sorte!'],
            'end': ['parabéns!', 'você conseguiu!', 'você é um verdadeiro mestre!', 'se quiser trabalhar no sigAmaes', 'fale comigo rs'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': '2',
        'questions': {
				0: {
					'title': 'Pergunta: 1',
					'description':'O que é o PM Canvas? ',
					'options': ['é um método para gerenciamento de projetos que permite, de uma forma colaborativa, envolver os membros de um time  \
                                     de desenvolvimento para estabelecer uma visão geral do projeto, permitindo que seja estabelecido na sequência o escopo do sistema a ser desenvolvido.',
                 				'Uma metodologia ágil para a execução de projetos baseada no Scrum.',
                                'Um software de gerenciamento de tarefas para equipes de projeto.',
                                'Um modelo exclusivo para cálculo de custos e orçamento de projetos'],
                    'correct': 0,
                    'link': '6',
				},
				1: {
					'title': 'Pergunta: 2',
					'description':'Qual é uma vantagem de se usar reuniões diárias assíncronas, como sugerido pelo LabES? ',
					'options': ['Elas permitem fazer ajustes nas histórias durante o sprint',
                 				'Evitam que o time compartilhe seu progresso frequentemente',
                                'Permitem ao cliente participar de cada etapa do desenvolvimento',
                                'Facilitam a comunicação entre membros de equipes com horários diferentes'],
                    'correct': 3,
                    'link': '6',
				},
				2: {
					'title': 'Pergunta: 3',
					'description':'Qual é o principal objetivo das Reuniões Diárias (Daily Scrum) durante o sprint?',
					'options': ['Revisar as metas do projeto e redefinir os prazos',
                 				'Atualizar os representantes dos clientes sobre o andamento do projeto',
                                'Melhorar a comunicação e sincronizar o trabalho entre os membros do time',
                                'Avaliar a qualidade do código desenvolvido'],
                    'correct': 2,
                    'link': '6',
				},
				3: {
					'title': 'Pergunta 4',
					'description':'Qual das alternativas descreve corretamente o objetivo principal de um MVP?',
					'options': ['Testar a viabilidade de um sistema no mercado com o menor conjunto de funcionalidades.',
                 				'Criar um produto completo para venda imediata.',
                                'Implementar todas as funcionalidades esperadas do produto final para evitar retrabalho.',
                                'Desenvolver um sistema de alta qualidade para atrair investidores.'],
                    'correct': 0,
                    'link': '6',
				},
				4: {
					'title': 'Pergunta 5',
					'description':'Como o Planning Poker ajuda o time a definir a estimativa das histórias?',
					'options': [' Ao fazer um sorteio aleatório para cada história.',
                 				' Ao permitir que cada desenvolvedor levante um cartão com a sua estimativa em story points, discutindo até chegar ao consenso.',
                                'Ao escolher as histórias com base na complexidade técnica, sem a participação dos clientes.',
                                'Ao medir o tempo necessário para concluir cada história em dias úteis.'],
                    'correct': 1,
                    'link': '6',
				},
				5: {
					'title': 'Pergunta 6',
					'description':'O que é registrado na aba "Sprints" do template de backlog do LabES?',
					'options': ['As tarefas concluídas de cada sprint.',
                 				'Os dados sobre cada sprint, incluindo ID, objetivos, datas e estatísticas de velocidade.',
                                'As histórias de usuário e suas descrições detalhadas.',
                                'Os nomes dos desenvolvedores responsáveis por cada tarefa.'],
                    'correct': 1,
                    'link': '6',
				},
				6: {
					'title': 'Pergunta 7',
					'description':'Qual é o principal benefício de calcular a velocidade da equipe após algumas iterações?',
					'options': ['Prever a quantidade de trabalho que a equipe consegue realizar em futuros sprints.',
                 				'Avaliar o desempenho individual de cada desenvolvedor.',
                                'Aumentar o número de sprints necessários para o projeto.',
                                'Reduzir o backlog automaticamente.'],
                    'correct': 0,
                    'link': '6',
				},
				7: {
					'title': 'Pergunta 8',
					'description':'Qual das seguintes informações NÃO é registrada na aba "Backlog" do template sugerido?',
					'options': ['Estimativa de esforço para cada história de usuário.',
                 				'Desenvolvedor responsável por implementar a história.',
                                'Notas e observações sobre as histórias de usuário.',
                                'Objetivos de cada sprint.'],
                    'correct': 3,
                    'link': '6',
				},
				8: {
					'title': 'Pergunta 9',
					'description':'Em qual situação é recomendado mover uma história do Backlog do Produto para o Backlog do Sprint? ',
					'options': ['Quando a história é de baixa importância e estimativa de esforço baixa',
                 				'Quando a história tem maior importância e seu esforço cabe no sprint planejado',
                                'Quando a história apresenta impedimentos significativos para o time',
                                'Quando a história já foi implementada anteriormente'],
                    'correct': 1,
                    'link': '6',
				},
				9: {
					'title': 'Pergunta 10',
					'description':'Durante a Revisão do Sprint, o que deve ser feito caso uma user story não seja aprovada? ',
					'options': ['Ela deve retornar para o Backlog do Produto para ser retrabalhada em um próximo sprint',
                 				'A user story deve ser descartada do backlog do projeto',
                                'O time deve ajustar a user story e apresentá-la novamente na mesma reunião',
                                'A user story é movida automaticamente para o backlog do próximo sprint'],
                    'correct': 0,
                    'link': '6',
				},
			},
		},
    'mae': {
        'name': 'tania',
		'dialog': {
            'default': ['TO CANSADA DE LAVAR LOUÇA NESSA CASA!!!', '...' ,'ja está indo meu filho?', 'só um segundo pro café ficar pronto'],
			'visited': ['prontinho hehe', 'eu disse que só levaria um segundo ^.^'],
            'end': ['parabéns filho!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': '4',
        'questions': {},
		},
    'pai': {
        'name': 'wilson',
		'dialog': {
            'default': ['o que será que eu leio hoje...', 'bom dia filho!', 'você ja está indo?', 'pegue café com sua mãe antes de sair!', 'nada melhor que um cafézinho para começar o dia!'],
			'visited': ['tenho 237 encomendas pra entregar hoje, é brincadeira!'],
            'end': ['parabéns filho!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    'luaninha': {
        'name': 'luana',
		'dialog': {
            'default': ['seja bem vindo ao labgrad', 'aqui voce pode usar os computadores a vontade para estudar', 'mas tem uma regra muito importante rs','faça silencio!'],
			'visited': ['seja bem vindo ao labgrad', 'aqui voce pode usar os computadores a vontade para estudar', 'mas tem uma regra muito importante rs','faça silencio!'],
            'end': ['seja bem vindo ao labes', 'a regra do silencio serve aqui também rs'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    'aninha': {
        'name': 'aninha',
		'dialog': {
            'default': ['bom dia irmão', 'não vá se esquecer de nada antes de sair', 'verifique sua mochila apertando a tecla "i"', 'boa sorte!'],
			'visited': ['vai logo!!'],
            'end': ['parabéns irmão!', 'você é o melhor!', 'sabia que voce conseguiria!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    'eliseu': {
        'name': 'eliseu',
		'dialog': {
            'default': ['vamo treinar!'],
			'visited': ['BIRRRLLLLLLL!!'],
            'end': ['parabéns irmão!', 'AGORA VAMOS TREINAR!!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    'angelus': {
        'name': 'angelus',
		'dialog': {
            'default': ['qual foi meu parceiro', 'a ufes é enorme e é muito fácil perder', 'as placas ajudam bastante', 'aperte "SPACEBAR" próximo a elas', 'boa sorte mano!'],
			'visited': ['aperte "SPACEBAR" próximo as placas elas para se localizar'],
            'end': ['boa meu parceiro!', 'seja bem vindo!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    'verdinho': {
        'name': 'verdinho',
		'dialog': {
            'default': [''],
			'visited': [''],
            'end': ['boa meu parceiro!', 'seja bem vindo!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    'roxinha': {
        'name': 'roxinha',
		'dialog': {
            'default': [''],
			'visited': [''],
            'end': ['boa meu parceiro!', 'seja bem vindo!'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    'azulzinha': {
        'name': 'azulzinha',
		'dialog': {
            'default': [''],
			'visited': [''],
            'end': ['tem café a vontade na geladeira', 'fique a vontade'],},
		'directions': ['down'],
		'visited': False,
        'end': False,
        'item': None,
        'questions': {},
		},
    }


# Dicionário com os dados dos itens do jogo
ITEMS_DATA = {
    '0': {
        'name': 'chave do vitor',
        'description':'é a prova de que voce conseguiu a aprovação do javaboy para entrar no sigamaes. você deve ter um alto conhecimento em java para pussuir esse item',
    },
    '1': {
		'name': 'chave da mona',
        'description':'estar em posso dessa chave significa que você tem domínio em git gitlab e gitlab flow, agora vá em frente e consiga a ultima chave',
    },
    '2': {
		'name': 'chave da patrícia',
        'description':'Parabéns, ter isso em seu inventário significa que você tem todas as três aprovações necessárias para entrar no labes, Parabéns!',
    },
    '4': {
		'name': 'cafe',
        'description':'Uma xícara de café forte e revigorante, feito com grãos de alta qualidade.' \
        '+ 50% velocidade 15 segundos\n "seu ótimo efeito combinado a sua curta duração pode se tornar viciante. CUIDADO"',
    },
}

# Dicionário com os links para os sites com as respostas das perguntas
# É necessário ter uma imagem nomeada com o valor da chave do dicionário na pasta /graphics/links de preferencia 108x108
# se não tiver a imagem o programa não iniciará pois é carregado no inicio do jogo os dados do computador
COMPUTER_DATA = {
    '0': {
        'title': 'Java - Jakarta ee - (Wildfly), PostgreSQL e Maven',
        'description':'O melhor conteudo de java da internet',
        'url': 'https://gitlab.labes.inf.ufes.br/labes/catalogo/-/wikis/plataformas/java,-jakarta-ee-(wildfly),-postgresql-e-maven#o-que-é',
        'color': 'violet',
	},
    '1': {
        'title': 'Git',
        'description':'catálogo labes - Guia Git',
        'url': 'https://gitlab.labes.inf.ufes.br/labes/catalogo/-/wikis/ferramentas/git',
        'color': 'black',
	},
    '2': {
        'title': 'Gitlab',
        'description':'Vatálogo labes - Guia Gitlab',
        'url': 'https://gitlab.labes.inf.ufes.br/labes/catalogo/-/wikis/ferramentas/git',
        'color': 'orange',
	},
    '3': {
        'title': 'HitLabES Glow',
        'description':'Vatálogo LabES - Guia gitlab flow',
        'url': 'https://gitlab.labes.inf.ufes.br/labes/catalogo/-/wikis/ferramentas/git',
        'color': 'purple',
	},
    '4': {
        'title': 'Java Keywords',
        'description':'palavras chave em java',
        'url': 'https://www.w3schools.com/java/java_ref_keywords.asp',
        'color': 'mid-blue',
	},
    '5': {
        'title': 'Docker - Dockerfile - Docker-Compose',
        'description':'catalogo labes - guia docker',
        'url': 'https://gitlab.labes.inf.ufes.br/labes/catalogo/-/wikis/ferramentas/Docker,-Dockerfile-e-docker-compose',
        'color': 'ocean',
	},
    '6': {
        'title': 'Processo Padrão Gerência de Projetos no LabES',
        'description':'Aprenda a gerenciar projetos no labes',
        'url': 'https://gitlab.labes.inf.ufes.br/labes/catalogo/-/wikis/procedimentos/processo-padrão-de-gerência-de-projetos-no-labes',
        'color': 'ocean',
	},
}

# Lista com as falas em caso de acerto em batalha do jogador
# 
CORRECTS_SPEAKS =[ 'vamos ver se voce é bom mesmo', 'Parabéns! Quem diria que você sabia a resposta.', 'Uau, acertou! Talvez você realmente saiba do que estamos falando aqui',
                  'Acertou de primeira? Vou anotar isso, é um milagre!', 'Ora, ora, parece que alguém andou estudando!', 'Ah, que surpresa agradável, você acertou!',
                  'Nossa, até me emocionei com essa resposta!', 'Ah, sabia que esse dia chegaria! Você acertou!', 'É, parece que milagres realmente acontecem!',
                  'Veja só, nem precisei desenhar pra você entender!','Finalmente', 'Parabéns! Quem diria que você sabia a resposta.', 'Uau, acertou! Talvez você realmente saiba do que estamos falando aqui',
                  'Acertou de primeira? Vou anotar isso, é um milagre!', 'Ora, ora, parece que alguém andou estudando!', 'Ah, que surpresa agradável, você acertou!',
                  'Nossa, até me emocionei com essa resposta!', 'Ah, sabia que esse dia chegaria! Você acertou!', 'É, parece que milagres realmente acontecem!',
                  'Veja só, nem precisei desenhar pra você entender!','Finalmente']

# Lista com as falas em caso de erro em batalha do jogador 
WRONGS_SPEAKS = ['Nossa, quase... só faltaram todos os detalhes certos!', 'Interessante! Só não foi a resposta que eu esperava.', 'Uau, passou longe! Mas foi uma tentativa original, eu diria.',
                  'Chegou bem perto... de errar tudo!', 'Interessante abordagem... só não se aplica a essa matéria.', 'Quase lá! Só faltou tudo!', 'Quase lá! Tipo... quase na mesma galáxia!',
                  'Que nteressante! Se estivéssemos falando de outra coisa.', 'É uma resposta! Só não para essa questão.', 'Você chegou lá! Só que no lugar errado.', 'Quase lá! Só que não.','Nossa, quase... só faltaram todos os detalhes certos!', 'Interessante! Só não foi a resposta que eu esperava.', 'Uau, passou longe! Mas foi uma tentativa original, eu diria.',
                  'Chegou bem perto... de errar tudo!', 'Interessante abordagem... só não se aplica a essa matéria.', 'Quase lá! Só faltou tudo!', 'Quase lá! Tipo... quase na mesma galáxia!',
                  'Que interessante! Se estivéssemos falando de outra coisa.', 'É uma resposta! Só não para essa questão.', 'Você chegou lá! Só que no lugar errado.', 'Quase lá! Só que não.',]

