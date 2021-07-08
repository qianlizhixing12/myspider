$(document).ready(function () {
    function attrget() {
        $.ajax({
            url: "/api/custom/attr/get.do",
            type: "GET",
            success: function (data) {
                if (data.succ) {
                    console.log(data.attrs)
                    let attrs = data.attrs;
                    for (key in attrs) {
                        if (key === 'tag') {
                            $(`input[name='${key}']`).importTags(attrs[key]);
                        } else if (key === 'area') {
                            $("select option[value='" + attrs[key] + "']").attr("selected", "selected");  //如果值一样 就选中对应的option
                        } else {
                            if ($(`input[name='${key}']`).length) {
                                $(`input[name='${key}']`).val(attrs[key]);
                            } else {
                                $(`textarea[name='${key}']`).val(attrs[key]);
                            }
                        }
                    }
                } else {
                    alert(data.msg);
                }
            },
        });
    }

    $("#resetattr").click(attrget);

    attrget();
});