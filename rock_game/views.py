from django.shortcuts import render ,redirect
import random

def check_winner(user_num):
	choices = ['stone','paper','scissor']
	choices_pic = ['media/rock.png','media/papers.png','media/scissor.png']
	n=random.randint(0,2)
	user_choice = choices[user_num]
	bot_choice = choices[n]

	d = dict()
	d['user_pic']=choices_pic[user_num]
	d['bot_pic']=choices_pic[n]
	
	if user_choice ==bot_choice:
		d['msg']='This is Tie'
	elif user_choice=='stone':
		if bot_choice=='paper':
			d['msg']='Paper covers Stone ....Computer won you loose'
		else:
			d['msg']='Stone breaks Scissor ....You Won'
	elif user_choice=='paper':
		if bot_choice=='scissor':
			d['msg']='Scissor cuts paper ....Computer won you loose'
		else:
			d['msg']='Paper covers Stone ....You Won'
	else:
		if bot_choice=='stone':
			d['msg']='Stone Breaks Scissor..... Computer won you loose'
		else:
			d['msg']='Scissor cuts paper ....You Won'
	return d

def home(request):
	return render(request,'home.html')

def rock(request):
	winner=check_winner(0)
	return render(request,'result.html',winner)

def paper(request):
	winner=check_winner(1)
	return render(request,'result.html',winner)

def scissor(request):
	winner=check_winner(2)
	return render(request,'result.html',winner)

