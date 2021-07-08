$(document).ready(function () {
    function customget() {
        $.ajax({
            url: "/api/custom/get.do",
            type: "GET",
            success: function (data) {
                if (data.succ) {
                    user = data.user;
                    $("input[name='email']").val(user.email);
                    $("input[name='username']").val(user.username);
                    $("input[name='first_name']").val(user.first_name);
                    $("input[name='last_name']").val(user.last_name);
                    $("input[name='password']").val(user.password);
                    $("input[id='date_joined']").val((new Date(user.date_joined)).toLocaleString());
                    $("input[id='last_login']").val((new Date(user.last_login)).toLocaleString());
                    // $("input[id='is_superuserY']").prop("checked", (user.is_superuser ? "checked" : ""));
                    // $("input[id='is_superuserN']").prop("checked", (user.is_superuser ? "" : "checked"));
                    // $("input[name='is_superuser'][value='" + (user.is_superuser ? 1 : 0) + "']").prop("checked", "checked");
                    // $("input[name='is_superuser'][value='" + (user.is_superuser ? 1 : 0) + "']").attr("checked", "checked");
                    user.is_superuser ? $("#is_superuserY").attr('checked', 'checked') : $("#is_superuserN").attr('checked', 'checked');
                } else {
                    alert(data.msg);
                }
            },
        });
    }

    // $("#savebase").click(function () {
    //     $.ajax({
    //         url: "/api/custom/edit.do",
    //         type: "POST",
    //         contentType: 'application/json;charset=utf-8',
    //         dataType: "json",
    //         data: JSON.stringify({
    //             "email": $("#email").val(),
    //             "username": $("#username").val(),
    //             "first_name": $("#first_name").val(),
    //             "last_name": $("#last_name").val(),
    //             "password": $("#password").val(),
    //         }),
    //         success: function (data) {
    //             alert(data.msg)
    //             cutomget();
    //         },
    //         error: function (err) {
    //             alert(err.responseJSON.msg)
    //         }
    //     });
    //     // form不发送请求
    //     return false;
    // });

    $("#resetcustom").click(customget);

    customget();
});