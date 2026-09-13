const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

const orders = [
  { id: 1, item: "Laptop", qty: 1 },
  { id: 2, item: "Mouse", qty: 2 }
];

app.get('/orders', (req, res) => {
  res.json({ service: "orders-service", version: process.env.APP_VERSION || "v1", orders });
});

app.get('/orders/health', (req, res) => {
  res.json({ status: "ok" });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`orders-service listening on port ${PORT}`);
});
