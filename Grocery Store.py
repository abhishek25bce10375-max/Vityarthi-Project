MNU = {
    "1. FRUITS": {
        "Apples (Royal Gala)": {"p": 240.00, "u": "kg", "stk": 20},
        "Bananas (MRL)": {"p": 32.00, "u": "kg", "stk": 30},
        "Watermelon (Kiran Big)": {"p": 125.00, "u": "kg", "stk": 10},
        "Musk Melon": {"p": 49.00, "u": "kg", "stk": 15},
        "Grapes (Imported Red Globe)": {"p": 69.00, "u": "kg", "stk": 25},
        "Pomegranate (Kesar)": {"p": 219.00, "u": "kg", "stk": 10},
        "Orange (Nagpur Premium)": {"p": 79.00, "u": "kg", "stk": 20},
        "Kiwi (Imported Zespri Green)": {"p": 149.00, "u": "kg", "stk": 8},
        "Mosambi": {"p": 64.00, "u": "kg", "stk": 25},
        "Pears (Green Imported)": {"p": 109.00, "u": "kg", "stk": 15},
    },
    "2. VEGETABLES": {
        "Amaranth Leaves": {"p": 18.00, "u": "kg"},
        "Beetroot": {"p": 40.00, "u": "kg"},
        "Bitter Gourd": {"p": 47.00, "u": "kg"},
        "Bottle Gourd": {"p": 38.00, "u": "kg"},
        "Brinjal (Common)": {"p": 43.00, "u": "kg"},
        "Cabbage": {"p": 35.00, "u": "kg"},
        "Capsicum": {"p": 57.00, "u": "kg"},
        "Carrot": {"p": 50.00, "u": "kg"},
        "Cauliflower": {"p": 33.00, "u": "kg"},
        "Coriander Leaves": {"p": 13.00, "u": "kg"},
        "Cucumber": {"p": 35.00, "u": "kg"},
        "Tomato": {"p": 36.00, "u": "kg"},
    },
    "3. MEAT": {
        "Chicken": {"p": 250.00, "u": "kg"},
        "Mutton": {"p": 650.00, "u": "kg"},
    },
    "4. FISH": {
        "Rohu (Rui)": {"p": 250.00, "u": "kg"},
        "Basa (Pangas)": {"p": 350.00, "u": "kg"},
        "Prawns (Medium/Large)": {"p": 800.00, "u": "kg"},
        "Seer Fish (Surmai/King Fish)": {"p": 950.00, "u": "kg"},
    },
    "5. SPICES (100g Pack)": {
        "Turmeric Powder (Haldi)": {"p": 40.00, "u": "100g"},
        "Chili Powder (Lal Mirch)": {"p": 55.00, "u": "100g"},
        "Coriander Powder (Dhania)": {"p": 35.00, "u": "100g"},
        "Cumin Powder (Jeera)": {"p": 90.00, "u": "100g"},
        "Garam Masala": {"p": 50.00, "u": "100g"},
        "Black Pepper (Kali Mirch)": {"p": 120.00, "u": "100g"},
    },
    "6. SAUCES & OILS": {
        "Tomato Ketchup": {"p": 85.00, "u": "500g"},
        "Mayonnaise": {"p": 100.00, "u": "400g"},
        "Mustard Sauce": {"p": 150.00, "u": "300g"},
        "Soy Sauce": {"p": 75.00, "u": "300ml"},
        "Refined Sunflower Oil": {"p": 110.00, "u": "500ml"},
        "Groundnut Oil": {"p": 130.00, "u": "500ml"},
        "Mustard Oil": {"p": 120.00, "u": "500ml"},
        "Coconut Oil": {"p": 150.00, "u": "500ml"},
        "Ghee (Clarified Butter)": {"p": 350.00, "u": "500ml"},
    },
    "7. SNACKS": {
        "Bonn Bourbon Cream Biscuit": {"p": 15.00, "u": "Small Packet"},
        "Cadbury Oreo Toffee Crunch": {"p": 50.00, "u": "116g Packet"},
        "Britannia Good Day Cookies": {"p": 50.00, "u": "75g Packet"},
        "Haldiram's Delhi Boondi Plain": {"p": 55.00, "u": "220g Packet"},
        "Roasted Almonds": {"p": 180.00, "u": "100g Packet"},
        "Mixed Dry Fruit": {"p": 220.00, "u": "100g Packet"},
    },
    "8. RICE": {
        "Basmati Rice (Premium)": {"p": 120.00, "u": "kg"},
        "Sona Masoori Rice": {"p": 60.00, "u": "kg"},
        "Boiled Rice": {"p": 50.00, "u": "kg"},
    }
}

CRT = []


def dsp_mnu():
    print("\n" + "="*50)
    print("  GROCERY SHOP MENU ")
    print("="*50)

    for cat, items in MNU.items():
        print(f"\n--- {cat} ---")
        i_cnt = 1
        for i_nm, dtl in items.items():

            print(f"{i_cnt:2}. {i_nm:40} ₹{dtl['p']:.2f} / {dtl['u']}")
            i_cnt += 1

def add_crt():
    
    while True:
        try:
            c_ch = input("\nEnter category number to select (e.g., 1 for Fruits): ") 
            c_ky = list(MNU.keys())[int(c_ch) - 1]
            sel_cat = MNU[c_ky]

            print(f"\n--- ITEMS in {c_ky} ---")
            i_lst = list(sel_cat.keys())
            for i, i_nm in enumerate(i_lst, 1):
                dtl = sel_cat[i_nm]
                print(f"{i:2}. {i_nm:40} ₹{dtl['p']:.2f} / {dtl['u']}")

            i_ch = int(input(f"\nEnter item number (1 to {len(i_lst)}) to add to cart: "))
            i_nm = i_lst[i_ch - 1]
            i_dtl = sel_cat[i_nm]

            unt = i_dtl['u']
            
            if 'kg' in unt:
                q_prm = f"Enter quantity for {i_nm} (in kg, e.g., 0.5 or 2): "
                qty = float(input(q_prm))
            elif 'Packet' in unt or 'g' in unt or 'ml' in unt:
                q_prm = f"Enter number of {unt} packets/units for {i_nm}: "
                qty = int(input(q_prm))
            else:
                q_prm = f"Enter quantity for {i_nm}: "
                qty = float(input(q_prm))

            tot_cst = i_dtl['p'] * qty

            CRT.append({
                "nm": i_nm,
                "p": i_dtl['p'],
                "u": i_dtl['u'],
                "q": qty,
                "t_cst": tot_cst
            })

            print(f" Added {qty} x {i_nm} to cart. Item cost: ₹{tot_cst:.2f}")
            break

        except (ValueError, IndexError):
            print(" Invalid input. Please enter a valid number from the menu.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


def vw_crt():
    
    print("\n" + "~"*50)
    print("  YOUR SHOPPING CART ")
    print("~"*50)

    if not CRT:
        print("Your cart is empty. Add some items!")
        return

    tot_bll = 0.0
    print(f"{'#':<3}{'Item':<40}{'Qty':<10}{'Unit Price':<15}{'Total Cost':<15}")
    print("-" * 83)

    for i, item in enumerate(CRT, 1):
        tot_bll += item['t_cst']
        unt = item['u']
        
        q_dsp = f"{item['q']:.2f}" if 'kg' in unt else f"{int(item['q'])}"

        print(f"{i:<3}{item['nm']:<40}{q_dsp + ' ' + unt.replace('g','').replace('ml','').replace('Packet',''):<10}₹{item['p']:.2f}{'':<4}₹{item['t_cst']:.2f}")

    print("-" * 83)
    print(f"{'':<65} **TOTAL BILL:** ₹{tot_bll:.2f}")
    print("~"*50)


def run_shp():
    """Main loop to run the grocery shop simulation."""
    while True:
        print("\n\n" + "*"*50)
        print("Welcome To VIT Bhopal Store")
        print("*"*50)
        print("Grocery Store Menu -")
        print("1. Show available items (by category)")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Exit")
        print("*"*50)

        ch = input("Enter your choice (1-4): ")

        if ch == '1':
            dsp_mnu()
        elif ch == '2':
            add_crt()
        elif ch == '3':
            vw_crt()
        elif ch == '4':
            vw_crt()
            print("\n" + "="*50)
            print(" Thank you for your purchase! You are supporting my business.")
            print("="*50)
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    run_shp()