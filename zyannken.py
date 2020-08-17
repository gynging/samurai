# -*- coding: utf-8 -*-
import random
'''
計算機とジャンケンをするプログラムを書きましょう。グー、チョキ、パーをそれぞれ0,1,2の整数で表すとします。森本さんの出す手を整数で入力し、勝負するようにします。コンピュータの出す手は乱数（同じ確率ででたらめに数を自動的に生成する仕組み）を使って作り出します。具体的には、random.randint(最小値, 最大値)という式を使うと自動的に最小値から最大値までのでたらめな整数を作ってくれます。
(プログラムの始めに、'import random'の宣言が必要)
 comp=random.randint(0,2)
こうすると、このcompに0か1か2の整数がでたらめに代入されます。
入力した森本さんの手とこのcompを比較して、ジャンケンの勝負を判定するプログラムを作って下さい。
実行結果
ジャンケンポン！
あなたは？(0:グー, 1:チョキ, 2:パー)> 0
わたしはチョキ。あなたはグー。あなたの勝ちです。
'''
print('ジャンケンポン！')
you = int(input('あなたは？(0:グー, 1:チョキ, 2:パー>)'))

comp=random.randint(0,2)

if comp == 0:#相手の手が0の場合
    print('わたしはグー。')
    if you == 0:
        print('あなたはグー。あいこです。')
    elif you == 1:
        print('あなたはチョキ。あなたの負けです。')
    else:
        print('あなたはパー。あなたの勝ちです。')

elif comp == 1: #相手の手が1の場合
    print('わたしはチョキ。')
    if you == 0:
        print('あなたはグー。あなたの勝ちです。')
    elif you == 1:
        print('あなたはチョキ。あいこです。')
    else:
        print('あなたはパー。あなたの負けです。')

else:#相手の手が2の場合
    print('わたしはパー。')
    if you == 0:
        print('あなたはグー。あなたの負けです。')
    elif you ==  1:
        print('あなたはチョキ。あなたの勝ちです。')
    else:
        print('あなたはパー。あいこです。')





