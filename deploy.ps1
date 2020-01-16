$CERT="~/Downloads/jb.pem"
$REMOTE="ec2-user@joysbirthday.com"

ssh -i $CERT $REMOTE "sudo systemctl stop nailedit"
ssh -i $CERT $REMOTE "sudo rm -rf ~ec2-user/nailedit"

scp -i $CERT -rp ./nailedit ${REMOTE}:~

ssh -i $CERT $REMOTE "chmod 755 ~/nailedit/*.sh"
ssh -i $CERT $REMOTE "sudo ~/nailedit/deploy_remote.sh"
ssh -i $CERT $REMOTE "sudo systemctl status nailedit"