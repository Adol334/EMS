from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income, Expense, AutomatedSaving, Advisory
from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect

#Add income page
@login_required
def add_income (request):
    if request.method == "POST":
        source = request.POST.get ("source")
        amount = request.POST.get ("amount")

        #Convert input to Decimal 
        decimal_amount = Decimal(amount) if amount else Decimal('0.00')

        #Create income record for logged-in user
        Income.objects.create(
            user=request.user,
            source=source,
            amount=decimal_amount
        )

        return redirect ("add_income")
    return render(request, "income.html")


#Add expense page
@login_required
def add_expense(request):

    if request.method == "POST":
        category = request.POST.get("category")
        amount = request.POST.get("amount")

        #Convert input to Decimal 
        decimal_amount = Decimal(amount) if amount else Decimal('0.00')
        
        #Save expense record
        Expense.objects.create(
            user=request.user,
            category=category,
            amount=decimal_amount
        )
 
        return redirect("add_expense")
    
    return render (request, "expense.html")


#Savings calculation page
@login_required
def saving(request):
    #Gets all incomes for logged-in user
    incomes = Income.objects.filter(user=request.user)
    
    #Calculates total income
    total_income = sum(i.amount for i in incomes) or Decimal('0.00')
    
    #Calculates 15% automated savings
    automated_savings = total_income * Decimal('0.15')

    context = {
        "total_income": total_income,
        "automated_savings": automated_savings,
    }
    
    return render(request, "saving.html", context)


#Financial report page
@login_required
def reports(request):
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    total_income = sum(i.amount for i in incomes) or Decimal('0.00')
    total_expenses = sum(e.amount for e in expenses) or Decimal('0.00')

    automated_savings = total_income * Decimal('0.15')
    
    #Remaining balance after expenses and savings
    balance = total_income - total_expenses - automated_savings

    context = {
        "incomes": incomes,
        "expenses": expenses,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "automated_savings": automated_savings,
        "balance": balance,
    }

    return render(request, "report.html", context)


#Advisory (financial tips) page
@login_required
def advisory(request):
    #Get tips for logged-in use
    student_tips = Advisory.objects.filter(user=request.user)
    
    #Packages the records inside the context dictionary
    context = {
        "tips": student_tips
    }
    
    #Pass the context directly to the HTML template
    return render(request, "advisory.html", context)


@login_required
def delete_income(request, pk):
    #Allows the user to delete their income records
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == "POST":
        income.delete()
    return redirect('report')


@login_required
def delete_expense(request, pk):
    #Allows the user to delete their expense records
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        expense.delete()
    return redirect('report')


