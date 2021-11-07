window.onload = function (message) {

    let add_order_auto = document.getElementById('add_order_auto');
    let add_order_hand = document.getElementById('add_order_hand');

    let products_list = JSON.parse(localStorage.getItem('products_list'));
    if (products_list == null) {
        products_list = [];
    }


    console.log('products_list---', products_list)

    function order_card_draw(product) {

        // console.log('table---', product)

        let orders_table = document.getElementById('orders_table');

        let order_card = document.createElement('tr');
        orders_table.appendChild(order_card);

        let cell_count = document.createElement('td');
        order_card.appendChild(cell_count);
        // cell_count.textContent = ;

        let cell_name = document.createElement('td');
        order_card.appendChild(cell_name);
        cell_name.textContent = product['field_name'];

        let cell_quantity = document.createElement('td');
        order_card.appendChild(cell_quantity);
        cell_quantity.textContent = product['field_quantity'];

        let cell_unit = document.createElement('td');
        order_card.appendChild(cell_unit);
        cell_unit.textContent = product['field_unit'];


        let cell_delete = document.createElement('td');
        let cell_delete_link = document.createElement('a');
        let cell_delete_i = document.createElement('i');
        cell_delete_link.setAttribute('href', '#');
        cell_delete_link.classList.add('delete-link');
        cell_delete_i.classList.add('fa');
        cell_delete_i.classList.add('fa-times');
        cell_delete_link.appendChild(cell_delete_i);
        cell_delete.appendChild(cell_delete_link);
        order_card.appendChild(cell_delete);

        orders_table.appendChild(order_card)

    }


// orders_form.appendChild()

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
        console.log('auto',product);
        products_list.push(product);
        localStorage.setItem('products_list', JSON.stringify(products_list));
        alert('products_list---')
        order_card_draw(product);
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
        console.log('hand', product)
        products_list.push(product);
        localStorage.setItem('products_list', JSON.stringify(products_list));
        alert('products_list---');
        order_card_draw(product);
    }


    function get_select(id) {
        return document.getElementById(id).selectedIndex
    }

}