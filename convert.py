import json
import collections
import csv

# For pre-processing the data and converted both json files into csv files
def preprocess (data):
  question = []
  qid = []
  is_impossible = []
  answer = []
  answer_sentence = []
  start_pos = 0
  end_pos = 0

  # Get the corrsponding context for this set of questions
  for k in range (len(data['data'])):
    for j in range (len(data['data'][k]['paragraphs'])):
      context = data['data'][k]['paragraphs'][j]['context']
      chars = list (context)

      for i in range (len(data['data'][k]['paragraphs'][j]['qas'])):
        question.append (data['data'][k]['paragraphs'][j]['qas'][i]['question'])
        qid.append (data['data'][k]['paragraphs'][j]['qas'][i]['id'])
        is_impossible.append (data['data'][k]['paragraphs'][j]['qas'][i]['is_impossible'])

        # In this case, no answer only the plausible answers are available
        if (data['data'][k]['paragraphs'][j]['qas'][i]['is_impossible']):
          if (len(data['data'][k]['paragraphs'][j]['qas'][i]['plausible_answers']) == 0):
            answer.append (" ")
            answer_sentence.append (" ")
            continue
          answer.append (data['data'][k]['paragraphs'][j]['qas'][i]['plausible_answers'][0]['text'])
          index = data['data'][k]['paragraphs'][j]['qas'][i]['plausible_answers'][0]['answer_start']

        else:
          ans_start = []
          ans_text = []
          for ans in data['data'][k]['paragraphs'][j]['qas'][i]['answers']:
            ans_start.append (ans['answer_start'])
            ans_text.append (ans['text'])

          start_ans = collections.Counter(ans_start)
          start_list = dict(start_ans)
          text_ans = collections.Counter(ans_text)
          test_list = dict(text_ans)

          # Find the highest frequency
          max_start= max(list(start_ans.values()))
          start_val = [num for num, freq in start_list.items() if freq == max_start]
          max_text= max(list(text_ans.values()))
          text_val = [num for num, freq in test_list.items() if freq == max_text]
          answer.append (text_val[0])
          index = start_val[0]

        for i in reversed (range (index)):
          if (i == 0):
            start_pos = 0
            break

          # When reach a possible starting position, we need to do further checking
          if (chars[i] == '.' or chars[i] == '!' or chars[i] == '?'):
            if (chars[i+1] == " " and chars[i+2].isupper()):
              # get rid of the stop sign and the space sign
              start_pos = i + 2
              break


        for i in range (index, len(chars)):
          if (i >= (len(chars) - 3)):
            end_pos = len(chars) - 1
            break

          # When reach a possible ending position, we need to do further checking
          if (chars[i] == '.' or chars[i] == '!' or chars[i] == '?'):
            if (chars[i+1] == " " and chars[i+2].isupper()):
              end_pos = i
              break

        answer_sentence.append (context[start_pos: (end_pos+1)])
  return qid, question, answer_sentence, answer, is_impossible


def main():
    with open('data/train.json') as f:
        data = json.load(f)

    qid, question, answer_sentence, answer, is_impossible = preprocess (data)
    with open('squad_train_v.csv', mode='w') as replace_file:
        file_writer = csv.writer(replace_file)
        file_writer.writerow(['id', 'question','answer_sentence', 'answer', 'is_impossible'])
        for i in range (len (question)):
          file_writer.writerow([qid[i], question[i], answer_sentence[i], answer[i], is_impossible[i]])

    with open("data/dev.json") as f_dev:
        data_dev = json.load(f_dev)

    qid, question, answer_sentence, answer, is_impossible = preprocess (data_dev)
    with open('squad_dev_v.csv', mode='w') as replace_file:
        file_writer = csv.writer(replace_file)
        file_writer.writerow(['id', 'question','answer_sentence', 'answer', 'is_impossible'])
        for i in range (len (question)):
          file_writer.writerow([qid[i], question[i], answer_sentence[i], answer[i], is_impossible[i]])



if __name__ == "__main__":
    main()
