from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey, UniqueConstraint
from src.external_interfaces.database.model.base import Base


class LayerRuleAssociation(Base):
    """
    Classe do sqlalchemy que mapeia a tabela layer_rule_association em banco
    """
    
    __tablename__ = 'layer_rule_association'

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    layer_id = Column(Integer, ForeignKey('layers.id'))
    rule_id = Column(Integer, ForeignKey('rules.id'))
    action = Column(Enum('refuse', 'pendency'), nullable=False)
    identify = Column(String, nullable=True, default='layer_rule_association')
    status = Column(Enum('active', 'inactive'), default='active', nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    __table_args__ = (UniqueConstraint('layer_id', 'rule_id'),)
