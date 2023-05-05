resource "aws_security_group" "security_group" {
  name = "${var.app_name}-alb"
  vpc_id = var.vpc_id
  dynamic "ingress" {
    for_each = var.ingress_ports
    iterator = port
    content {
      from_port   = port.value
      to_port     = port.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "${var.app_name}-sg"
  }
}

resource "aws_elb" "alb" {
  name               = "melchior-alb"
  load_balancer_type = "application"
  security_groups = [aws_security_group.security_group.id]
  subnets         = var.public_subnet_ids
}
