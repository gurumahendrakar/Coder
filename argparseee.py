import argparse


x = argparse.ArgumentParser(description='This Is Like you',usage='This Is for adding some digits saveing your time!!',)
x.add_argument('num1',help='this two numbers adding')
x.add_argument('num2',help='this two numbers adding')
x.add_argument('num3',help='this two numbers adding')

xx = x.parse_args()

print(int(xx.num1) + int(xx.num2) + int(xx.num3))
