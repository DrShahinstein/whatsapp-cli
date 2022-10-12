# whatsapp-cli

A command line interface for helpful whatsapp-web operations like scheduling messages and so on.

## Requirements

- [python-poetry](https://python-poetry.org/)

## Installation

```bash
$ git clone https://www.github.com/DrShahinstein/whatsapp-cli.git
$ cd whatsapp-cli/
$ poetry install
```

## Usage

```bash
[whatsapp-cli]$ poetry run python3 -m whatsapp-cli [commands] [options]
```

## Examples

### How to schedule messages?

Let's create two new schedules like so...

```bash
[whatsapp-cli]$ poetry run python3 -m whatsapp-cli create schedule
The name of your schedule: test1
Message: Test message.
Receiving phone number: +## ### ### ####
hh:mm: 22
hh:mm: 18
New schedule created.
```

```bash
[whatsapp-cli]$ poetry run python3 -m whatsapp-cli create schedule
The name of your schedule: test2
Message: Test message.
Receiving phone number: +## ### ### ####
hh:mm: 22
hh:mm: 15
New schedule created.
```

---

And here, let's create a schedule which is going to be removed soon to see how you can remove schedules.

```bash
[whatsapp-cli]$ poetry run python3 -m whatsapp_cli create schedule
The name of your schedule: Gonna be removed
Message: Test message.
Receiving phone number: +## ### ### ####
hh:mm: 23
hh:mm: 50
New schedule created.
```

---

Here, as you can see, we removed the schedule named "Gonna be removed"

```bash
[whatsapp-cli]$ poetry run python3 -m whatsapp_cli remove schedule
Enter the name of the schedule you want to remove: Gonna be removed
Gonna be removed removed.
Enter the name of the schedule you want to remove: ^CAborted!
```

---

Finally, we currently have two messages, let's schedule them.

```bash
[whatsapp-cli]$ poetry run python3 -m whatsapp_cli schedule
# The CLI firstly picks the earliest one among our schedules and starts a countdown.
Next message will be delivered in 0:00:44
# After the ending of the countdown, it goes on with the next one.
Next message will be delivered in 0:02:50
```

The delivery of a message means that the CLI is going to open up whatsapp-web on your default browser and deliver your message after some seconds.

## Contribution

Pull requests are always welcome. This project, for now, only works with just scheduling whatsapp-web messages but it's been developed in an improvable way so that it can have many more operations than just scheduling messages with either open-source support and also my effort.
Apart from that, if you like this project, please don't forget to leave a star.
