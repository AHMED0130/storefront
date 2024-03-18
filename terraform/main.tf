provider "aws" {
  region = "eu-north-1"  
}


resource "aws_security_group" "example" {
  name        = var.security-group-name
  description = "Example security group for EC2 instance"
  
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }
  ingress  {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 

  } 
  
  ingress  {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 

  } 
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  
  }
}

data "aws_ami" "this" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
  filter {
    name   = "name"
    values = ["al2023-ami-2023*"]
  }
}



resource "aws_instance" "server" {
  ami                          = data.aws_ami.this.id
  associate_public_ip_address  = true
  instance_type                = var.instance-type
  key_name                     = var.key-name
  security_groups = [aws_security_group.example.name]
  user_data = file("script.sh")
  
  tags = {
    environment = "${var.env_prefix}-env"
  }
               
}



output "public_ip" {
  value = aws_instance.server.public_ip
}