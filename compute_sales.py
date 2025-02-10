'''
This script is used to compute the total cost for all sales included
in the second JSON file.
1. Reads the two JSON files: product catalog and sales data.
2. Computes all total sales based on the price catalogue
3. Performs time elasped and time calculation.
4. Prints results to SalesResults.txt amd console
'''

import sys
import time
import json


# Read JSON File
def read_json_file(file_name):
    """
    Reads two json files.
    JSON FILE 1: Contains product catalog (prices).
    JSON FILE 2: Contains the sales data.
    Throw exception if file can't be read or found.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in file {file_name}.")
        sys.exit(1)


# Compute Total Sales
def create_price_catalogue(products):
    """Create a price catalogue dictionary based on product titles."""
    price_catalogue = {}
    for product in products:
        price_catalogue[product['title']] = product['price']
    return price_catalogue


def calculate_total_sales(sales_data, price_catalogue):
    """Calculate the total sales based on the price catalogue."""
    total_sales = 0
    for sale in sales_data:
        product_name = sale['Product']
        quantity = sale['Quantity']
        # Find the price for the product in the catalogue
        if product_name in price_catalogue:
            total_sales += price_catalogue[product_name] * quantity
        else:
            print(f"Warning: Product '{product_name}' not found.")
    return total_sales


# Printing Results
def print_results(total_sales, elapsed_time, calculation_time):
    '''
    Print results in console and output file SalesResults.txt.
    '''
    result_output = (
        f"TC3\n"
        f"TOTAL SALES: {total_sales:.2f}\n"
        f"TIME ELAPSED FOR EXECUTION: {elapsed_time:.6f} seconds\n"
        f"TIME FOR DATA CALCULATION: {calculation_time:.6f} seconds\n"
    )
    # Print to console
    print(result_output)

    # Write to file
    with open("SalesResults.txt", 'w', encoding='utf-8') as file:
        file.write(result_output)


# Main Function
def main():
    '''
    The main function will execute all the functions.
    THe elasped time and calcaultion time is calculated within this function.
    '''
    # Start time measurement
    start_time = time.time()

    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py file1 file2")
        sys.exit(1)

    # Read the file
    file_path = (
        "C:\\Users\\raria\\OneDrive\\Documents\\VS Projects\\"
        "Pruebas_Software\\Actividad5.2\\Compute Sales\\TC3\\"
    )
    catalog = read_json_file(file_path + "priceCatalogue.json")
    sales = read_json_file(file_path + "salesRecord.json")

    # Start Calculation Time
    calculation_start_time = time.time()

    # Create Price Catalogue and Compute Sales
    price_catalogue = create_price_catalogue(catalog)
    total_sales = calculate_total_sales(sales, price_catalogue)

    # Determine Calculation Time
    calculation_end_time = time.time()
    calculation_time = calculation_end_time - calculation_start_time

    # Calculate Elapsed Time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print and save results
    print_results(total_sales, elapsed_time, calculation_time)


if __name__ == "__main__":
    main()
