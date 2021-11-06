window.onload = function (message) {
    let add_order_auto = document.getElementById('add_order_auto');
    let add_order_hand = document.getElementById('add_order_hand');


    let products_list = JSON.parse(localStorage.getItem('products_list'));
    if (products_list == null) {
        products_list = [];
    }
    console.log('product_list', products_list)


    add_order_auto.onclick = function () {
        let product = {
            field_name: document.getElementById('value-name1').options[get_select('value-name1')].text,
            field_type: document.getElementById('value-name2').value,
            field_diameter: document.getElementById('value-name3').options[get_select('value-name3')].text,
            field_thickness: document.getElementById('value-name4').options[get_select('value-name4')].text,
            field_quantity: document.getElementById('value-name5').value,
            field_unit: 'Выбор из списка',
            field_note: document.getElementById('feed_msg2').value
        }
        console.log(product);
        products_list.push(product)
        localStorage.setItem ('products_list', JSON.stringify(products_list));
    }

    add_order_hand.onclick = function () {
        let product = {
            field_name: document.getElementById('value-name7').value,
            field_type: 'Пользовательский выбор',
            field_diameter: 'Пользовательский выбор',
            field_thickness: 'Пользовательский выбор',
            field_quantity: document.getElementById('value-name8').value,
            field_unit: document.getElementById('value-name9').value,
            field_note: document.getElementById('feed_msg').value
        }
        console.log(product)
        products_list.push(product)
        localStorage.setItem ('products_list', JSON.stringify(products_list));
    }


}

function get_select(id) {
    return document.getElementById(id).selectedIndex
}

