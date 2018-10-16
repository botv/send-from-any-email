const sendgrid = require('sendgrid')

sendgrid.send({
  to: 'benbotvinick@gmail.com',
  from: {
      email: 'pearce_crocker19@milton.edu',
      name: 'Pearce Crocker'
  },
  subject: 'eat my ass.',
  text: 'Please devour my booty hole.'
});
