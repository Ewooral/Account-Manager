$(()=>{

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: (xhr) => {
            xhr.setRequestHeader("X-CSRFTOKEN", csrftoken)
        }
    })

    // add account func
    $(document).on('submit', '.account_form', function (event) {
        event.preventDefault();
        $('#posting_data').slideDown(100, function () {
            $(this).html('Sending your data please wait.....').slideUp(9500);
        });
        const accountName = document.getElementById('account_name');
        const accountLogin = document.getElementById('account_login');
        const accountPassword = document.getElementById('account_password');
        const serverName = document.getElementById('server_name');
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: {
                "account_name": accountName.value,
                "account_login": accountLogin.value,
                "account_password": accountPassword.value,
                "server_name": serverName.value,
            },
            dataType: 'json',
            success: function (response) {
                $("#mt_accounts_section").html(response['form']);
                $("input").val('');
            },
            error: function (rs, e) {
                console.log(rs.responseText);
            }
        });
    });

    // remove account func
    $(document).on("click", "#remove_account_button", (event) => {
        event.preventDefault();
    
        var formData = $("#account_delete_form").serialize();
        var id = $("#remove_account_button").attr("value");

        $.ajax({
            type: "POST",
            url: `/account/${id}/delete/`,
            data: formData,
            dataType: "json",
            success: (response) => {
                $("#remove_account_section").html(response["uaccount"]);
                
            },
            error: (rs, e) => {
                console.log(rs.responseText);
            },
        });
    });
})