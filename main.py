from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
dt = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':

        country = {"Côte d Ivoire": 7, 'Vietnam': 35, "Nigeria": 23, "Zambia": 36, 'Rwanda': 25, 'Haiti': 14,
                   "Tanzania": 32, 'Ethiopia': 9, 'Guyana': 13, 'Zimbabwe': 37, 'Namibia': 22, 'Mozambique': 21,
                   'Botswana': 3, 'Kenya': 15, 'Uganda': 34, 'Congo DRC': 6, 'Burundi': 14,
                   'Dominician Republic': 8,
                   'South Sudan': 29, 'Ghana': 10, 'Swaziland': 31, 'Benin': 2, 'Senegal': 26, 'Mali': 20,
                   'South Africa': 28, 'Afghanishan': 0, 'Cameroon': 5, 'Malawi': 19, 'Togo': 33, 'Angola': 1,
                   'Libya': 18,
                   'Guatemala': 11, 'Guinea': 12, 'Liberia': 17, 'Pakistan': 24, 'Sierra Leone': 27}
        Country = request.form['Country']
        for i in country.keys():
            if i == Country:
                Country = country[i]
                Country=int(Country)
                break

        Fulfill_Via = request.form['Fulfill Via']
        if Fulfill_Via == 'Direct Drop':
            Fulfill_Via = 0
        else:
            Fulfill_Via = 1

        shipmentmode = {'Air': 0, 'Air Charter': 1, 'Ocean': 2, 'Truck': 3}
        shipment_mode = request.form['Shipment Mode']
        for j in shipmentmode.keys():
            if j == shipment_mode:
                Shipment_mode = shipmentmode[j]
                Shipment_mode = int(Shipment_mode)
        productgroup = {'HRDT': 3, 'ARV': 2, 'ACT': 0, 'ANTM': 1, 'MRDT': 4}
        product_Group = request.form['Product Group']
        for k in productgroup.keys():
            if k == product_Group:
                Product_Group = productgroup[k]
                Product_Group = int(Product_Group)

        Unit_of_Measure = int(request.form['Unit of Measure (Per Pack)'])
        Line_Item_Quantity = int(request.form['Line Item Quantity'])
        Pack_Price = float(request.form['Pack Price'])
        Unit_Price = float(request.form['Unit Price'])
        Weight = float(request.form['Weight (Kilograms)'])
        Scheduled_Delivery_Date_Year = int(request.form['Scheduled Delivery Date Year'])
        Scheduled_Delivery_Date_Month = int(request.form['Scheduled Delivery Date Month'])
        Scheduled_Delivery_Date_Day = int(request.form['Scheduled Delivery Date Day'])

        prediction=dt.predict([[Country, Fulfill_Via, Shipment_mode, Product_Group,
                                  Unit_of_Measure, Line_Item_Quantity,
                                  Pack_Price, Unit_Price, Weight, Scheduled_Delivery_Date_Year,
                                  Scheduled_Delivery_Date_Month, Scheduled_Delivery_Date_Day]])
        output=round(prediction[0],2)

        if output < 0:
            return render_template('index.html', prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html', prediction_text="The Estimate Freight Cost is {}".format(output))
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)

