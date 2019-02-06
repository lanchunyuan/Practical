import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
capitalsItems = list(capitals.items())

for quizNum in range(35):
    # quizFile = open(f'capitalsquiz-{(quizNum+1):02d}.txt','w')
    answerKeyFile = open(f'capitalsquiz_answers-{(quizNum+1):02d}.txt','w')
    # print(f'capitalsquiz-{quizNum:02d}.txt')
    with open(f'capitalsquiz-{(quizNum + 1):02d}.txt', 'a') as f_obj:
        f_obj.write('Name:\n\nDate:\n\nPeriod:\n\n')
        f_obj.write((' '*20) + f'State Capitals Quiz (Form {quizNum + 1})')
        f_obj.write('\n\n')
    # quizFile.write('Name:\n\nDate:\n\n\Period:\n\n')
    # quizFile.write((' '*20) + f'State Capitals Quiz (Form {quizNum + 1})')
    # quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        with open(f'capitalsquiz-{(quizNum + 1):02d}.txt', 'a') as f_obj:
            f_obj.write(f'{(questionNum+1):02d}. What is the capital of {states[questionNum]}?\n')
            for i in range(4):
                f_obj.write(f'    {"ABCD"[i]}. {answerOptions[i]}\n')
            f_obj.write('\n')
        # quizFile.write(f'{(questionNum+1):02d}. What is the capital of {states[questionNum]}?\n')
        # for i in range(4):
        #     quizFile.write('    {\'ABCD\'[i]}. {answerOptions[i]}\n')
        # quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    answerKeyFile.close()
