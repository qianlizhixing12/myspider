$(document).ready(function () {
    {% for updatedt in updatedts %}
    $('#{{ updatedt.updatedt }}').DataTable({
        serverSide: true,
        ajax: function (data, callback, settings) {
            //封装请求参数
            var param = {};
            param.updatedt = '{{ updatedt.updatedt }}';
            param.schoolkey = data.search.value;
            param.length = data.length; //页面显示记录条数，在页面显示每页显示多少项的时候
            param.start = data.start; //开始的记录序号
            //ajax请求数据
            $.ajax({
                url: '/api/gaokao/scoollist/get.do',
                type: 'POST',
                cache: false, //禁用缓存
                data: JSON.stringify(param), //传入组装的参数
                dataType: "json",
                contentType: 'application/json;charset=utf-8',
                success: function (result) {
                    //封装返回数据
                    var returnData = {};
                    returnData.draw = data.draw; //这里直接自行返回了draw计数器,应该由后台返回
                    returnData.recordsTotal = result.recordsTotal; //返回数据全部记录
                    returnData.recordsFiltered = result
                        .recordsTotal; //后台不实现过滤功能，每次查询均视作全部结果
                    returnData.length = result
                        .length; //页面显示记录条数，在页面显示每页显示多少项的时候
                    returnData.start = result.start; //开始的记录序号
                    // returnData.page = (result.start / result.length) + 1; //当前页码
                    returnData.data = result.data; //返回的数据列表
                    //console.log(returnData);
                    //调用DataTables提供的callback方法，代表数据已封装完成并传回DataTables进行渲染
                    //此时的数据需确保正确无误，异常判断应在执行此回调前自行处理完毕
                    callback(returnData);
                }
            });
        },
        "ordering": false,
        "searching": true, //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        "processing": true,
        "paging": true,
        "pageNumber": 1, //初始化加载第一页，默认第一页
        "pageLength": 20, //每页的记录行数（*）
        "lengthMenu": [20, 50, 100], //可供选择的每页的行数（*）
        "pagingType": "full_numbers",
        "info": true,
        //  "dom": '<"top"lf>t<"bottom"ip><"clear">',
        // buttons: {
        //     name: 'primary',
        //     buttons: [ 'copy', 'csv', 'excel' ]
        // },
        fixedHeader: {
            footer: true
        },
        language: {
            "decimal": "",
            "emptyTable": "表中记录为空",
            "info": "显示第 _START_ 至 _END_ 条记录， 共 _TOTAL_ 条记录",
            "infoEmpty": "显示第 0 至 0 条记录，共 0 条记录",
            "infoFiltered": "(由 _MAX_ 条记录过滤)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "分页调整 _MENU_",
            "loadingRecords": "载入中...",
            "processing": "处理中...",
            "search": "查找",
            "zeroRecords": "没有匹配记录",
            "paginate": {
                "first": "首页",
                "last": "尾页",
                "next": "下页",
                "previous": "上页"
            },
            "aria": {
                "sortAscending": ": 升序排列",
                "sortDescending": ": 降序排列"
            }
        },
        columns: [{
            "title": "序号",
            // "data": "name",
            "cellType": "th",
            "searchable": false,
            "orderable": false,
            // "createdCell": function (td, cellData, rowData, row, col) {
            //     if (row < 1) {
            //         $(td).css('color', 'red');
            //     }
            // },
            "render": function (data, type, row, meta) {
                return meta.row + 1;

            },

        },
        {
            "title": "院校名称",
            "data": "name",
            "searchable": true,
            "orderable": true,
        },
        {
            "title": "院校所在地",
            "data": 'city',
            "searchable": false,
            "orderable": false,
        },
        {
            "title": "教育行政主管部门",
            "data": "dep",
            "searchable": false,
            "orderable": false,
        },
        {
            "title": "院校类型",
            "data": "style",
            "type": "date",
            "searchable": false,
            "orderable": false,
        },
        {
            "title": "学历层次",
            "data": "level",
            "searchable": false,
            "orderable": false,
        },
        {
            "title": "满意度",
            "data": "star",
            "width": "20px",
            "searchable": false,
            "orderable": false,
            "render": function (data, type, full, meta) {
                return data + '<i class="success fa fa-long-arrow-up"></i>';
            }
        },
        ],

    });
    {% endfor %}
});