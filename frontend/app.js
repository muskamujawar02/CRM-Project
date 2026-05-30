const API_URL = "";

async function createTicket() {

    const customer_name = document.getElementById("customer_name").value;
    const customer_email = document.getElementById("customer_email").value;
    const subject = document.getElementById("subject").value;
    const description = document.getElementById("description").value;

    const response = await fetch(`${API_URL}/api/tickets`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            customer_name,
            customer_email,
            subject,
            description
        })
    });

    const data = await response.json();

    alert(`Ticket Created: ${data.ticket_id}`);

    loadTickets();
}

async function loadTickets() {

    const search = document.getElementById("search").value;
    const status = document.getElementById("statusFilter").value;

    let url = `${API_URL}/api/tickets?`;

    if (search) {
        url += `search=${search}&`;
    }

    if (status) {
        url += `status=${status}`;
    }

    const response = await fetch(url);

    const tickets = await response.json();

    const table = document.getElementById("ticketTable");

    table.innerHTML = "";

    tickets.forEach(ticket => {

        let statusClass = "";

        if (ticket.status === "Open") {
            statusClass = "status-open";
        }
        else if (ticket.status === "In Progress") {
            statusClass = "status-progress";
        }
        else {
            statusClass = "status-closed";
        }

        table.innerHTML += `
            <tr onclick="openTicket('${ticket.ticket_id}')" style="cursor:pointer">
                <td>${ticket.ticket_id}</td>
                <td>${ticket.customer_name}</td>
                <td>${ticket.subject}</td>
                <td class="${statusClass}">${ticket.status}</td>
                <td>${ticket.created_at}</td>
            </tr>
        `;
    });
}

function openTicket(ticket_id) {

    localStorage.setItem("ticket_id", ticket_id);

    window.location.href = "detail.html";
}

loadTickets();

const darkModeBtn = document.getElementById("darkModeBtn");

darkModeBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
});