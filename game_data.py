CHARACTERS_DATA = {
	'char_1': {
		'dialog': {
			'default': ['voce entendeu?'], 
			'visited': ['Parabens poh voce é brabo', 'potato']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'questions': {},
		},
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
            'default': ['então você conseguiu chegar até aqui!', 'devo parabenizá-lo', 'mas daqui você não passa!', 'sou conhecido como javaboy', 'para conseguir a minha chave você terá que me vencer em uma batalha!', 'você aceita o desafio?'],
			'visited': ['parabéns!', 'você conseguiu mostrar domínio teórico em java', 'meus parabéns!', 'agora vá conseguir a aprovação da monalessa', 'sei que você consegue' ,'boa sorte!']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': '0',
        'questions': {
				0: {
					'title': 'Pergunta 1',
					'description':'Você e sua equipe estão atuando no desenvolvimento de um sistema para a plataforma de educação online. Um dos membros da equipe apresentou uma dúvida sobre a utilização do comando “try..catch..finally”.',
					'options': ['Um bloco opcional que contém o código a ser executado sempre, independentemente de ocorrer ou não uma exceção. ',
                 				'Um bloco reservado apenas para manipulação de erros críticos. ',
                                'Um bloco que só é executado se uma exceção for lançada. ',
                            	'Um bloco utilizado para interromper o fluxo do programa imediatamente ao encontrar uma exceção. '],
                    'correct': 0,
                    'link': '1',
				},
				1: {
					'title': 'Pergunta 2',
					'description':'Descrição da pergunta 2',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '1',
				},
				2: {
					'title': 'Pergunta 3',
					'description':'Descrição da pergunta 3',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '1',
				},
				3: {
					'title': 'Pergunta 4',
					'description':'Descrição da pergunta 4',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '1',
				},
				4: {
					'title': 'Pergunta 5',
					'description':'Descrição da pergunta 5',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '1',
				},
				5: {
					'title': 'Pergunta 6',
					'description':'Descrição da pergunta 6',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				6: {
					'title': 'Pergunta 7',
					'description':'Descrição da pergunta 7',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				7: {
					'title': 'Pergunta 8',
					'description':'Descrição da pergunta 8',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				8: {
					'title': 'Pergunta 9',
					'description':'Descrição da pergunta 9',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				9: {
					'title': 'Pergunta 10',
					'description':'Descrição da pergunta 10',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',	
				},
			},
		},
    'monalessa': {
		'name': 'Monalessa',
		'dialog': {
            'default': ['então voce foi aprovado pelo java master, vitor', 'nada mal', 'vamos ver se você é bom em gerencia de projetos!!!'],
			'visited': ['meus parabéns!', 'você acertou x questões', 'vamos! pegue isso você vai precisar!']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': '1',
        'questions': {
				0: {
					'title': 'Pergunta 1',
					'description':'Descrição da pergunta 1',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				1: {
					'title': 'Pergunta 2',
					'description':'Descrição da pergunta 2',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				2: {
					'title': 'Pergunta 3',
					'description':'Descrição da pergunta 3',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				3: {
					'title': 'Pergunta 4',
					'description':'Descrição da pergunta 4',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				4: {
					'title': 'Pergunta 5',
					'description':'Descrição da pergunta 5',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				5: {
					'title': 'Pergunta 6',
					'description':'Descrição da pergunta 6',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				6: {
					'title': 'Pergunta 7',
					'description':'Descrição da pergunta 7',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				7: {
					'title': 'Pergunta 8',
					'description':'Descrição da pergunta 8',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				8: {
					'title': 'Pergunta 9',
					'description':'Descrição da pergunta 9',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
				9: {
					'title': 'Pergunta 10',
					'description':'Descrição da pergunta 10',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
				},
			},
		},
    'patricia': {
        'name': 'Patricia',
		'dialog': {
            'default': ['seja bem vindo!', 'então voce conseguiu as outras duas chaves', 'isso não significa nada se você não conseguir a minha!', 'aqui acaba para você! muahahaha'],
			'visited': ['uauu', 'voce conseguiu superar o meu desafio', 'você merece isso!', 'com isso você tem todas as chaves!', 'agora que desafio de verdade', 'você pode entrar no sigAmaes', 'boa sorte!']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': '2',
        'questions': {
				0: {
					'title': 'Pergunta 1',
					'description':'Descrição da pergunta 1',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				1: {
					'title': 'Pergunta 2',
					'description':'Descrição da pergunta 2',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				2: {
					'title': 'Pergunta 3',
					'description':'Descrição da pergunta 3',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				3: {
					'title': 'Pergunta 4',
					'description':'Descrição da pergunta 4',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				4: {
					'title': 'Pergunta 5',
					'description':'Descrição da pergunta 5',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				5: {
					'title': 'Pergunta 6',
					'description':'Descrição da pergunta 6',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				6: {
					'title': 'Pergunta 7',
					'description':'Descrição da pergunta 7',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '0',
				},
				7: {
					'title': 'Pergunta 8',
					'description':'Descrição da pergunta 8',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '1',
				},
				8: {
					'title': 'Pergunta 9',
					'description':'Descrição da pergunta 9',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '1',
				},
				9: {
					'title': 'Pergunta 10',
					'description':'Descrição da pergunta 10',
					'options': ['A', 'B', 'C', 'D'],
                    'correct': 0,
                    'link': '1',
				},
			},
		},
    'mae': {
        'name': 'tania',
		'dialog': {
            'default': ['TO CANSADA DE LAVAR LOUÇA NESSA CASA!!!', '...' ,'ja está indo meu filho?', 'só um segundo pro café ficar pronto'],
			'visited': ['prontinho hehe', 'eu disse que só levaria um segundo ^.^']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': '4',
        'questions': {},
		},
    'pai': {
        'name': 'wilson',
		'dialog': {
            'default': ['o que será que eu leio hoje...', 'bom dia filho!', 'você ja está indo?', 'pegue café com sua mãe antes de sair!', 'nada melhor que um cafézinho para começar o dia!'],
			'visited': ['tenho 237 encomendas pra entregar hoje, é brincadeira!']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': None,
        'questions': {},
		},
    'luaninha': {
        'name': 'luana',
		'dialog': {
            'default': ['seja bem vindo ao labgrad', 'aqui voce pode usar os computadores a vontade para estudar', 'mas tem uma regra muito importante rs','faça silencio!'],
			'visited': ['seja bem vindo ao labgrad', 'aqui voce pode usar os computadores a vontade para estudar', 'mas tem uma regra muito importante rs','faça silencio!']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': None,
        'questions': {},
		},
    'aninha': {
        'name': 'ana',
		'dialog': {
            'default': ['bom dia irmão', 'não vá se esquecer de nada antes de sair', 'verifique sua mochila apertando a tecla "i"', 'boa sorte!'],
			'visited': ['vai logo!!']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': None,
        'questions': {},
		},
    'angelus': {
        'name': 'angelo',
		'dialog': {
            'default': ['qual foi meu parceiro', 'é muito fácil se perder na ufes', 'as placas ajudam bastante', 'aperte "BACKSPACE" próximo a elas', 'boa sorte mano!'],
			'visited': ['qual foi meu parceiro', 'é muito fácil se perder na ufes', 'as placas ajudam bastante', 'aperte "BACKSPACE" próximo a elas', 'boa sorte mano!']},
		'directions': ['down'],
		'look_around': True,
		'visited': False,
        'item': None,
        'questions': {},
		},
    }


ITEMS_DATA = {
    '0': {
        'name': 'chave do vitor',
        'description':'chave do vitor, é a prova de que voce conseguiu a aprovação do javaboy para entrar no sigamaes. você deve ter um alto conhecimento em java para pussuir esse item',
    },
    '1': {
		'name': 'chave da mona',
        'description':'chave da mona, é a prova de que voce conseguiu a aprovação da monalessa para entrar no sigamaes',
    },
    '2': {
		'name': 'chave da patrícia',
        'description':'chave da patrícia, é a prova de que voce conseguiu a aprovação da patricia para entrar no sigamaes',
    },
    '4': {
		'name': 'cafe',
        'description':'Uma xícara de café forte e revigorante, feito com grãos de alta qualidade.' \
        '+ 50% velocidade 15 segundos\n "seu ótimo efeito combinado a sua curta duração pode se tornar viciante. CUIDADO"',
    },
}

COMPUTER_DATA = {
    '0': {
        'title': 'Java',
        'description':'Aqui você pode aprender e testar seus conhecimentos em Java',
        'url': 'https://www.google.com',
        'color': 'gray',
	},
    '1': {
        'title': 'Github',
        'description':'O melhor site para aprender git e versionamento de código',
        'url': 'https://www.google.com',
        'color': 'white',
	},
    
	
        
}
