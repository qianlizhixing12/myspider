$(document).ready(function () {
    Morris.Bar({
        element: 'scrapy-graph',
        data: {{ static_info.data | safe }},
    xkey: '{{ static_info.xkey }}',
    ykeys: {{ static_info.ykey | safe }},
    labels: {{ static_info.labels | safe }},
    barRatio: 0.4,
    barColors: ['#26B99A', '#34495E', '#ACADAC', '#3498DB'],
    xLabelAngle: 35,
    hideHover: 'auto',
    resize: true
    });
});