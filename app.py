from flask import Flask, jsonify, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bullet.html')
def bullet():
    return render_template('bullet.html') 
    

@app.route('/bulletChart.html')
def bulletChart():
    return render_template('bulletChart.html') 
    

@app.route('/crossfilter.html')
def crossfilter():
    return render_template('crossfilter.html') 
    

@app.route('/crossfilterWithDimentions.html')
def crossfilterWithDimentions():
    return render_template('crossfilterWithDimentions.html') 
    

@app.route('/crossfilterWithTables.html')
def crossfilterWithTables():
    return render_template('crossfilterWithTables.html') 
    

@app.route('/cumulativeLineChart.html')
def cumulativeLineChart():
    return render_template('cumulativeLineChart.html') 
    

@app.route('/discreteBarChart.html')
def discreteBarChart():
    return render_template('discreteBarChart.html') 
    

@app.route('/historicalBar.html')
def historicalBar():
    return render_template('historicalBar.html') 
    

@app.route('/historicalBarChart.html')
def historicalBarChart():
    return render_template('historicalBarChart.html') 
    

@app.route('/horizon.html')
def horizon():
    return render_template('horizon.html') 
    

@app.route('/indentedtree.html')
def indentedtree():
    return render_template('indentedtree.html') 
    

@app.route('/legend.html')
def legend():
    return render_template('legend.html') 
    

@app.route('/line.html')
def line():
    return render_template('line.html') 
    

@app.route('/lineChart.html')
def lineChart():
    return render_template('lineChart.html') 
    

@app.route('/lineChartSVGResize.html')
def lineChartSVGResize():
    return render_template('lineChartSVGResize.html') 
    

@app.route('/linePlusBarChart.html')
def linePlusBarChart():
    return render_template('linePlusBarChart.html') 
    

@app.route('/linePlusBarWithFocusChart.html')
def linePlusBarWithFocusChart():
    return render_template('linePlusBarWithFocusChart.html') 
    

@app.route('/lineWithFisheyeChart.html')
def lineWithFisheyeChart():
    return render_template('lineWithFisheyeChart.html') 
    

@app.route('/lineWithFocusChart.html')
def lineWithFocusChart():
    return render_template('lineWithFocusChart.html') 
    

@app.route('/multiBar.html')
def multiBar():
    return render_template('multiBar.html') 
    

@app.route('/multiBarChart.html')
def multiBarChart():
    return render_template('multiBarChart.html') 
    

@app.route('/multiBarHorizontalChart.html')
def multiBarHorizontalChart():
    return render_template('multiBarHorizontalChart.html') 
    

@app.route('/multiChart.html')
def multiChart():
    return render_template('multiChart.html') 
    

@app.route('/parallelCoordinates.html')
def parallelCoordinates():
    return render_template('parallelCoordinates.html') 
    

@app.route('/pie.html')
def pie():
    return render_template('pie.html') 
    

@app.route('/pieChart.html')
def pieChart():
    return render_template('pieChart.html') 
    

@app.route('/scatter.html')
def scatter():
    return render_template('scatter.html') 
    

@app.route('/scatterChart.html')
def scatterChart():
    return render_template('scatterChart.html') 
    

@app.route('/scatterPlusLineChart.html')
def scatterPlusLineChart():
    return render_template('scatterPlusLineChart.html') 
    

@app.route('/sparkline.html')
def sparkline():
    return render_template('sparkline.html') 
    

@app.route('/sparklinePlus.html')
def sparklinePlus():
    return render_template('sparklinePlus.html') 
    

@app.route('/stackedArea.html')
def stackedArea():
    return render_template('stackedArea.html') 
    

@app.route('/stackedAreaChart.html')
def stackedAreaChart():
    return render_template('stackedAreaChart.html') 
    

@app.route('/test/lineChartTest.html')
def test_lineChartTest():
    return render_template('test/lineChartTest.html') 
    

@app.route('/test/pieChartTest.html')
def test_pieChartTest():
    return render_template('test/pieChartTest.html') 
    

@app.route('/test/ScatterChartTest.html')
def test_ScatterChartTest():
    return render_template('test/ScatterChartTest.html') 
    

@app.route('/test/stackedAreaChartTest.html')
def test_stackedAreaChartTest():
    return render_template('test/stackedAreaChartTest.html') 
    

@app.route('/test/multiBarChartTest.html')
def test_multiBarChartTest():
    return render_template('test/multiBarChartTest.html') 
    

@app.route('/test/polylinearTest.html')
def test_polylinearTest():
    return render_template('test/polylinearTest.html') 
    

@app.route('/test/realTimeChartTest.html')
def test_realTimeChartTest():
    return render_template('test/realTimeChartTest.html') 

@app.route('/images/grey-plus.png')
def test_realTimeChartTest():
    return send_file('static/images/grey-plus.png', mimetype='image/png')

@app.route('/images/grey-minus.png')
def test_realTimeChartTest():
    return send_file('static/images/grey-minus.png', mimetype='image/png')

@app.route('/images/nvd3_sampleLineChart1.png')
def test_realTimeChartTest():
    return send_file('static/images/nvd3_sampleLineChart1.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, port=8000)