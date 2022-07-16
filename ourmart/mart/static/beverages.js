$(document).ready(function(){
    $('.buttons').click(function(){
        $(this).addClass('active').siblings().removeClass('active');

        let filter = $(this).attr('data-filter');
        if(filter == 'all'){
            $('.picture').show(400);
        }else{
            $('.picture').not('.'+ filter).hide(200);
            $('.picture').filter('.'+ filter).show(400);
        }
    })
})
