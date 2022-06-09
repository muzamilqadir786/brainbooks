
jQuery(document).ready(function() {
    $("#boardsDropdown").change(function () {
        var url = $("#boardsForm").attr("boards-drop-url");  // get the url of the `load_cities` view
        var boardId = $(this).val();  // get the selected country ID from the HTML input
        $.ajax({
            type: "POST",// initialize an AJAX request
            url: url, // 'ajax/load-dropdown/',                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            dataType: "json",
            data: {
                'board_id': boardId       // add the country id to the GET parameters
            },

            success: function (data) {   // `data` is the return of the `load_cities` view function
//          $("#class-names").html(data);  // replace the contents of the city input with the data that came from the server
//            console.log(data);
                $("#classNamesDropdown").empty();
                $("#classNamesDropdown").append('<option> Select Class </option>');
                $.each(data.context.classes, function (i, item) {
//                console.log(item);
                    $('#classNamesDropdown').append($('<option>', {
                        value: item.id,
                        text: item.name
                    }));
                });//each closed
            } //success closed
        }); //ajax closed

    });
    $("#classNamesDropdown").change(function () {
        var url = $("#classesForm").attr('classes-drop-url');
        var classId = $(this).val();
//                  alert(classId);
        $.ajax({
            type: "POST",
            url: url,
            dataType: "json",
            data: {
                'class_id': classId
            },

            success: function (data) {
//                console.log(data);
                $("#subjectNamesDropdown").empty();
                $("#subjectNamesDropdown").append('<option> Select Subject </option>');
                $.each(data.context.subjects, function (i, item) {
//                        console.log(item);
                    $("#subjectNamesDropdown").append($('<option>', {
                        value: item.subject_id,
                        text: i + 1 + ') ' + item.name

                    })); //append closed
                });
            }//success closed

        }); //ajax closed

    });//change closed

    $("#subjectNamesDropdown").change(function () {
        var url = $("#subjectsForm").attr('subjects-drop-url');
        var subjectId = $(this).val();
//                  alert(subjectId);
        $.ajax({
            type: "POST",
            url: url,
            dataType: "json",
            data: {
                'subject_id': subjectId
            },

            success: function (data) {
//                  alert(data);
                console.log(data);
                $("#chapterNamesDropDown").empty();
                $("#chapterNamesDropDown").append('<option> Select Chapter </option>');
                $.each(data.context.chapters, function (i, item) {
                    console.log(item);
                    $("#chapterNamesDropDown").append($('<option>', {
                        value: item.chapter_id,
                        text: item.name

                    })); //append closed
                });
            }//success closed

        }); //ajax closed

    });//change closed
});//ready closed