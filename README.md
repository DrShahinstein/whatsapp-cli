# whatsapp-cli

Simple command line tool for whatsapp-web featuring message schedules. 

## Requirements

- [python-poetry](https://python-poetry.org/)
- [python-pip](https://pypi.org/project/pip/)

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

Let's create two new schedules like so:

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
# The CLI first picks the earliest one among our schedules and starts a countdown.
Next message will be delivered in 0:00:44
# After the ending of the countdown, it goes on with the next one.
Next message will be delivered in 0:02:50
```

The delivery of a message means that the CLI is going to open up whatsapp-web on your default browser and deliver your message after 10 seconds.

## Build

To build whatsapp-cli, you need to run:

```bash
[whatsapp-cli]$ poetry build
```

Just then you run `poetry build`, a new directory `dist` is going to be created. Change your directory to this directory and build whatsapp-cli with the whl file inside `dist` by running:

```bash
[dist]$ pip3 install whatsapp_cli-0.1.0-py3-none-any.whl
```

Now that you have built whatsapp-cli, you can run it this way:

```bash
$ whatsapp_cli [commands] [options]
```
