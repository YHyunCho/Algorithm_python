def solution(numbers, hand):
    answer = ''
    lastLeftnum = []
    lastRightnum = []

    for i in range(len(numbers)) :

      if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7 :
        answer += 'L'
        lastLeftnum.append(numbers[i])

      elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9 :
        answer += 'R'
        lastRightnum.append(numbers[i])

      else :
        leftnum = numbers[i] - lastLeftnum[-1]
        rightnum = numbers[i] - lastRightnum[-1]

        if leftnum > rightnum :
          answer += 'R'
          lastRightnum.append(numbers[i])

        elif leftnum < rightnum :
          answer += 'L'
          lastLeftnum.append(numbers[i]) 

        else :
          if hand == 'right' :
            answer += 'R'
            lastRightnum.append(numbers[i])

          else :
            answer += 'L'
            lastLeftnum.append(numbers[i])


    print(lastLeftnum)
    print(lastRightnum)
    print(answer)


    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
solution(numbers, hand)