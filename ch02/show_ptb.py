import sys
sys.path.append('..')
from dataset import ptb

corpus, word_to_id, id_to_word = ptb.load_data('train')

print('corpus size:', len(corpus))
print('corpus[:30]', corpus[:30])
print()
print('id_to_word[0]:', id_to_word[0])
print('id_to_word[1]:', id_to_word[1])
print('id_to_word[2]:', id_to_word[2])
print('id_to_word[car]:', word_to_id['car'])
print('id_to_word[happy]:', word_to_id['happy'])
print('id_to_word[lexus]:', word_to_id['lexus'])
