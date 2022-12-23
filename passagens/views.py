from django.shortcuts import render
from passagens.forms import PassagensForms, PessoaForms

def index(request):

    form = PassagensForms()
    pessoas_form = PessoaForms()
    contexto ={'form':form, 'pessoa_form': pessoas_form}
    return render(request, 'index.html',contexto)

def revisaoConsulta(request):
    if request.method == 'POST':
        form =PassagensForms(request.POST)
        pessoaForm =PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'form':form, 'pessoaForm':pessoaForm}
            return render(request, 'minha_consulta.html',contexto)
        else:
            print('Form invalido')
            contexto = {'form':form, 'pessoaForm':pessoaForm}
            return render(request, 'index.html',contexto)
