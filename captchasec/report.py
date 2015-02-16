#!/usr/bin/env python
# -*- coding : utf-8 -*-
from io import open
from datetime import datetime


class Report():
    """
    Class for generate report by user choice
    """
    def __init__(self, captcha_list, report_type):
        self.captcha_list = captcha_list
        self.report_type = report_type

    def generate(self):
        """
        Generate report.
        :return:
        """
        if self.report_type == "csv":
            self.csv_report()
        elif self.report_type == "json":
            self.json_report()
        else:
            self.html_report()

    def json_report(self):
        """
        Import json library in order to write results to the file.
        :return:
        """
        import json
        print "Generating JSON report."
        f_name = "result_{0}.json".format(datetime.now().strftime("%m-%d-%y-%H:%M:%S"))
        with open(f_name, "w") as f:
            output = json.dumps(self.captcha_list, indent=2, sort_keys=True)
            f.write(unicode(output))
            f.close()
        print "Results are saved into {}".format(f_name)

    def csv_report(self):
        """
        Import csv library in order to write results to the csv file.
        :return:
        """
        import csv
        print "Generating CSV report."
        f_name = "result_{0}.csv".format(datetime.now().strftime("%m-%d-%y-%H:%M:%S"))
        with open(f_name, 'wb') as f:
            wr = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            for i in self.captcha_list:
                wr.writerow([i['image'], i['answer'], i['time']])
        print "Results are saved into {}".format(f_name)

    def html_report(self):
        table_content = u""
        for id, item in enumerate(self.captcha_list):
            table_content += u"""
            <tr>
              <th scope="row">%s</th>
              <td><img src="file://%s"></img></td>
              <td>%s</td>
              <td><input type="checkbox" class="correct" checked></td>
            </tr>
            """ % (id, item['image'], item['answer'])

        html_template = u"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Captchasec - Captcha Difficulty tester</title>
            <!-- Bootstrap -->
            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet">
            <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
            <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
            <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
            <![endif]-->
            <script src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
            <script src="http://code.highcharts.com/highcharts.js"></script>
            <script src="http://code.highcharts.com/modules/exporting.js"></script>
            <script>
                $(function () {{
                    chartOptions = ({{
                        chart: {{
                            renderTo: 'container',
                            plotBackgroundColor: null,
                            plotBorderWidth: 0,
                            plotShadow: false
                        }},
                        title: {{
                            text: 'Success<br>rates',
                            align: 'center',
                            verticalAlign: 'middle',
                            y: 50
                        }},
                        tooltip: {{
                            pointFormat: '{{series.name}}: <b>{{point.percentage:.1f}}%</b>'
                        }},
                        plotOptions: {{
                            pie: {{
                                dataLabels: {{
                                    enabled: true,
                                    distance: -50,
                                    style: {{
                                        fontWeight: 'bold',
                                        color: 'white',
                                        textShadow: '0px 1px 2px black'
                                    }}
                                }},
                                startAngle: -90,
                                endAngle: 90,
                                center: ['50%', '75%']
                            }}
                        }},
                        series: [{{
                            type: 'pie',
                            name: 'Browser share',
                            innerSize: '50%',
                            data: [
                                ['Correct',   1],
                                ['Incorrect',   0],
                            ]
                        }}]
                    }});
                    // Handler
                    graph = new Highcharts.Chart(chartOptions);
                    $('.correct').change(function(){{
                        graph.series[0].setData([$('.correct:checkbox:checked').size(),
                            $('.correct:checkbox:not(:checked)').size()],true);
                    }})
                }});
            </script>
        </head>
        <body>
        <div class="container">
            <div class="header">
                <h3 class="text-muted">Captchasec</h3>
            </div>
            <div id="container"></div>

            <div class="row">
                <div class="col-md-12">
                    <table class="table table-striped">
                      <thead>
                        <tr>
                          <th>#</th>
                          <th>Image</th>
                          <th>Answer</th>
                          <th>Is correct ?</th>
                        </tr>
                      </thead>
                      <tbody>
                        {0}
                      </tbody>
                    </table>
                </div>
            </div>
            <footer class="footer">
                <p>&copy; Generated by captchasec v0.0.1</p>
            </footer>
        </div>
        <!-- /container -->
        </body>
        </html>
        """.format(table_content)
        f_name = "result_{}.html".format(datetime.now().strftime("%m-%d-%y-%H:%M:%S"))
        with open(f_name, "w") as f:
            f.write(html_template)
        print "Results are saved into {}".format(f_name)