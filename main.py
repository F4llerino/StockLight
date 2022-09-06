import tkinter
import tkinter.messagebox
import yfinance as yf
from tkinter import *


#Variables
ticker = ""
counter_red = 0
counter_yellow = 0
counter_green = 0


#Funktionen
def get_company_name(tick):
    try:
        info = yf.Ticker(tick).info
        if info:
            if 'longName' in info:
                return info['longName']
    except NameError:
        print("No Name found")


def get_ticker():
    global ticker
    get_entry = ticker_entry.get()

    if len(get_entry) <= 10:
        ticker = get_entry
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Company not found!")
        ticker_entry.delete(0, "end")


def show_red():
    global red_img

    red_img = PhotoImage(file="C:\\Users\\luisf\\PycharmProjects\\StockLight\\images\\Ampel_rot.png")
    red_label = Label(main_frame, image=red_img)
    red_label.grid(column=1, row=4, columnspan=2)


def show_yellow():
    global yellow_img
    yellow_img = PhotoImage(file="C:\\Users\\luisf\\PycharmProjects\\StockLight\\images\\Ampel_Gelb.png")
    yellow_label = Label(main_frame, image=yellow_img)
    yellow_label.grid(column=1, row=4, columnspan=2)


def show_green():
    global green_img
    green_img = PhotoImage(file="C:\\Users\\luisf\\PycharmProjects\\StockLight\\images\\Ampel_gruen.png")
    green_label = Label(main_frame, image=green_img)
    green_label.grid(column=1, row=4, columnspan=2)


def show_red_yellow():
    global red_yellow_img
    red_yellow_img = PhotoImage(file="C:\\Users\\luisf\\PycharmProjects\\StockLight\\images\\Ampel_gelb_rot.png")
    red_yellow_label = Label(main_frame, image=red_yellow_img)
    red_yellow_label.grid(column=1, row=4, columnspan=2)


def show_green_yellow():
    global green_yellow_img
    green_yellow_img = PhotoImage(file="C:\\Users\\luisf\\PycharmProjects\\StockLight\\images\\Ampel_gruen_gelb.png")
    green_yellow_label = Label(main_frame, image=green_yellow_img)
    green_yellow_label.grid(column=1, row=4, columnspan=2)


def liquidity(cash, short_term_investments, net_receivables, total_current_liab):
    try:
        return ((cash + short_term_investments + net_receivables) / total_current_liab) * 100
    except TypeError:
        return ((cash + net_receivables) / total_current_liab) * 100


def short_term_invest(df):
    try:
        sti = df.loc["Short Term Investments"]
        return (sti.iloc[0] + sti.iloc[1] + sti.iloc[2]) / 3
    except KeyError:
        return 0


def calculate_short_term_inv(ca, sti, nr, tcl):
    try:
        return ((ca + sti + nr) / tcl) * 100
    except TypeError:
        return ((ca + nr) / tcl) * 100


def analyse():
    #Variables
    global counter_red, counter_yellow, counter_green
    get_ticker()
    print(ticker)

    # Get_Finance_Data
    t = yf.Ticker(ticker)
    t_balance = t.balance_sheet
    t_financials = t.financials

    try:
        ticker_info = t.info
        print(ticker_info)
    except TypeError:
        tkinter.messagebox.showwarning(title="Warning", message="Error: wrong input!")

    # DataFrames
    cash_df = t_balance.loc["Cash"]
    total_stockholder_equity_df = t_balance.loc["Total Stockholder Equity"]
    total_liab_df = t_balance.loc["Total Liab"]
    total_current_liab_df = t_balance.loc["Total Current Liabilities"]
    net_receivables_df = t_balance.loc["Net Receivables"]
    net_income_df = t_financials.loc["Net Income"]

    # Average_Numbers
    cash = (cash_df.iloc[0] + cash_df.iloc[1] + cash_df[2]) / 3
    short_term_investments = short_term_invest(t_balance)
    total_stockholder_equity = (total_stockholder_equity_df[0] + total_stockholder_equity_df[1] +
                                total_stockholder_equity_df[2]) / 3
    total_liab = (total_liab_df[0] + total_liab_df[1] + total_liab_df[2]) / 3
    total_current_liab = (total_current_liab_df[0] + total_current_liab_df[1] + total_current_liab_df[2]) / 3
    net_receivables = (net_receivables_df[0] + net_receivables_df[1] + net_receivables_df[2]) / 3
    net_income = (net_income_df[0] + net_income_df[1] + net_income_df[2]) / 3

    # Kennzahlen
    roi = (net_income / (total_stockholder_equity + total_liab)) * 100
    eigenkapitalquote = (total_stockholder_equity / (total_stockholder_equity + total_liab)) * 100
    liquiditaet_2 = calculate_short_term_inv(cash, short_term_investments, net_receivables, total_current_liab)

    #IF-Conditions to get the base of the recommendation
    if roi < 5:
        counter_red += 1
    elif 5 <= roi <= 7.5:
        counter_yellow += 1
    elif roi > 7.5:
        counter_green += 1

    if eigenkapitalquote < 50:
        counter_red += 1
    elif 50 <= eigenkapitalquote <= 65:
        counter_yellow += 1
    elif eigenkapitalquote > 65:
        counter_green += 1

    if liquiditaet_2 < 80:
        counter_red += 1
    elif 80 <= liquiditaet_2 < 100:
        counter_yellow += 1
    elif liquiditaet_2 >= 100:
        counter_green += 1

    print(counter_red)
    print(counter_yellow)
    print(counter_green)

    if counter_red == 3:
        show_red()
    elif counter_yellow == 3 or counter_yellow == 2:
        show_yellow()
    elif counter_green == 3:
        show_green()
    elif counter_red == 2:
        if counter_yellow == 1:
            show_red_yellow()
        else:
            show_yellow()
    elif counter_green == 2:
        if counter_yellow == 1:
            show_green_yellow()
        else:
            show_yellow()

    #End of Function
    change_label(roi, eigenkapitalquote, liquiditaet_2)
    counter_red = 0
    counter_yellow = 0
    counter_green = 0
    print(counter_red)
    print(counter_yellow)
    print(counter_green)


def change_label(r, eig, liq):
    global roi_result_var, eigenkapitalquote_result_var,\
        liquiditaet_result_var, company_var

    co_name = get_company_name(ticker)
    company_var.set("")
    roi_result_var.set("")
    eigenkapitalquote_result_var.set("")
    liquiditaet_result_var.set("")
    root.update()
    company_var.set(co_name)
    roi_result_var.set(str(round(r, 2)) + "%")
    eigenkapitalquote_result_var.set(str(round(eig, 2)) + "%")
    liquiditaet_result_var.set(str(round(liq, 2)) + "%")


#Gui
root = Tk()
root.title("StockLight 1.0")
root.geometry("500x750")
main_frame = Frame(root)
main_frame.pack()

#StringVar
company_var = tkinter.StringVar()
roi_result_var = tkinter.StringVar()
eigenkapitalquote_result_var = tkinter.StringVar()
liquiditaet_result_var = tkinter.StringVar()

company_var.set("")
roi_result_var.set("")
eigenkapitalquote_result_var.set("")
liquiditaet_result_var.set("")

#Widgets
header = Label(main_frame, text="Enter a ticker", font="Verdana 14 bold")
ticker_entry = Entry(main_frame)
submit_button = Button(main_frame, text="Submit", font="Verdana 10 bold", bg="magenta2", command=analyse)

#Name_&_Numbers
company_label = Label(main_frame, textvariable=company_var, font="Verdana 14 underline bold", fg="blue")
roi_label = Label(main_frame, text="Return on Investment:", font="Verdana 12 bold")
eigenkapitalquote_label = Label(main_frame, text="Eigenkapitalquote:", font="Verdana 12 bold")
liquiditaet_2_label = Label(main_frame, text="Liquidität 2. Grades:", font="Verdana 12 bold")

roi_result_label = Label(main_frame, textvariable=roi_result_var, font="Verdana 12 bold")
eigenkapitalquote_result_label = Label(main_frame, textvariable=eigenkapitalquote_result_var, font="Verdana 12 bold")
liquiditaet_2_result_label = Label(main_frame, textvariable=liquiditaet_result_var, font="Verdana 12 bold")

#Layout
header.grid(column=1, row=1, columnspan=2, pady=25)
ticker_entry.grid(column=1, row=2, columnspan=2, ipady=5)
submit_button.grid(column=1, row=3, columnspan=2, pady=20)

#Name_&_Numbers
company_label.grid(column=1, row=5, columnspan=2)
roi_label.grid(column=1, row=6)
eigenkapitalquote_label.grid(column=1, row=7)
liquiditaet_2_label.grid(column=1, row=8)

roi_result_label.grid(column=2, row=6)
eigenkapitalquote_result_label.grid(column=2, row=7)
liquiditaet_2_result_label.grid(column=2, row=8)

root.mainloop()
