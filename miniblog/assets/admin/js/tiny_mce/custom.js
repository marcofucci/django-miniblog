
function setupCustomTinyMCE(ed, mediaURL) {

    // Add a custom Insert Image button
    var $insert_image_temp = $('body').append($('<input type="hidden" id="insert_image_temp" />'));
    ed.addButton('insertimage', {
        title : 'Insert image',
        image : mediaURL + 'admin/img/img-add.png',
        onclick : function() {
            // this will populate html element with image url
            $insert_image_temp.val('');
            djangoFileBrowser('insert_image_temp', '/', 'image', window);
            if ($insert_image_temp.val()) {
                alert($insert_image_temp.val())
            }
        }
    });

}