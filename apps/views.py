from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import request
from django.contrib.redirects.models import Redirect


from apps.forms import AppForm1



def index(request):
       return render(request,'apps/step.html')
    
# def step1(request):
#      
#     wizard = wizard(request, WIZARD_STEPS)
#     my_form = ContactForm1(initial=wizard.data.get('step1_data', {}))
# 
#     if request.method == 'POST':
#         my_form = ContactForm1(request.POST)
# 
#         if my_form.is_valid():
#             wizard.set_data({'step1_data': my_form})
#             return Redirect(wizard.steps[1]['url'])
# 
#     return render(request, 'step.html', {'wizard': wizard, 'my_form': my_form})
# 
# 
# @wizard_check_id(redirect_to='wizard-step1')
# @wizard_check_data(['step1_data'], redirect_to='wizard-step1')
# def step2(request):
#     wizard = wizard(request, WIZARD_STEPS)
#     form1 = ContactForm1(initial=wizard.data.get('step2_data1', {}))
#     form2 = ContactForm2(initial=wizard.data.get('step2_data2', {}))
# 
#     if request.method == 'POST':
#         form1 = ContactForm1(request.POST)
#         form2 = ContactForm2(request.POST)
# 
#         if form1.is_valid() and form2.is_valid():
#             wizard.set_data({'step2_data1': form1, 'step2_data2': form2})
# 
#             return R(wizard.steps[2]['url'])
# 
#     return render(request, 'step.html', {'wizard': wizard, 'form1': form1, 'form2': form2})
# 
# 
# @wizard_check_id(redirect_to='wizard-step1')
# @wizard_check_data(['step2_data1', 'step2_data2'], redirect_to='wizard-step1')    
# def preview(request):
#     wizard = Wizard(request, WIZARD_STEPS)
# 
#     if 'confirm' in request.GET:
#         my_form = MyForm(wizard.data['post'])
#         form1 = MyForm1(wizard.data['post'])
#         form2 = MyForm2(wizard.data['post'])
# 
#         if my_form.is_valid() and form1.is_valid() and form2.is_valid():
#             my_form.save()
#             form1.save()
#             form2.save()
#             wizard.cleanup()
# 
#             return redirect('wizard-done')
# 
#     return render(request, 'preview.html', {'wizard': wizard})